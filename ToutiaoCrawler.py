import asyncio
import time

from pyppeteer import launch
from pyppeteer.network_manager import Response
from pyppeteer.page import Page

async def crawl_response(
        start_url: str, actions: list,
        response_match_callback: callable = None,
        response_handle_callback: callable = None,
):
    """

    A highly abstracted function can perform amost any puppeteer based spider task.
    Ignore the existence of any js encryption.

    :param start_url: init page url
    :param actions: a list of actions to perform on a Page object,
        each action should accept exact one argument.

        for example:

        async def click_by_xpath(page: Page):
            await asyncio.sleep(3)
            elemHandlers = await page.xpath(xpath)
            elemHandler = elemHandlers[0]
            await elemHandler.click()

    :param response_match_callback: a callback function determine whether should take actions on a response.
        this function should be a `async` function and accept exact one argument.

        for example:

        1. match all response
            lambda res: True
        2. match response with 'api' in its url
            lambda res: "api" in res.url
        3. match all xhr and fetch response
            def response_match_callback(res : Response):
                resourceType = res.request.resourceType
                    if resourceType in ['xhr', 'fetch']:
                        return True

    :param response_handle_callback: for those response match response_match_callback.
        this function should be a `async` function and accept exact one argument.

        for example:

        1. simply print response text
        async def response_handle_callback(res: Response):
            text = await res.text()
            print(text)

        2. save response to filesystem
        async def response_handle_callback(res: Response):
            text = await res.text()
            with open('example.json', 'w', encoding = 'utf-8') as f:
                f.write(text)
    :return:
    """

    async def intercept_response(res: Response):
        if response_match_callback:
            match = await response_match_callback(res)
            if match:
                await response_handle_callback(res)

    browser = await launch({
        'headless': False,
        'devtools': False,
        'args': [
            '-start-maximized',
            '--disable-extensions',
            '--hide-scrollbars',
            '--disable-bundled-ppapi-flash',
            '--mute-audio',
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-gpu',
            '--disable-infobars',
            '--enable-automation',
        ],
        'dumpio': True,
    })

    try:
        page = await browser.newPage()
        await page.goto(start_url)
        page.on('response', intercept_response)
        for task_action in actions:
            await task_action(page)
    finally:
        await browser.close()



async def main():
    # 爬取 https://www.toutiao.com/ feed 流数据
    start_url = "https://www.toutiao.com/"

    def click_by_xpath(xpath: str):
        async def _click(page: Page):
            await asyncio.sleep(3)
            elemHandlers = await page.xpath(xpath)
            elemHandler = elemHandlers[0]
            await elemHandler.click()

        return _click

    actions = []
    tabs = ["推荐", "热点", "科技", "娱乐", "游戏", "体育", "财经", "搞笑"]
    for tabname in tabs:
        xpath = "//span[contains(text(),'{}')]".format(tabname)
        action = click_by_xpath(xpath)
        actions.append(action)

    async def is_feed_api(res: Response):
        return "api/pc/feed" in res.url

    async def print_response_text(res: Response):
        text = await res.text()
        print(text)

    await crawl_response(start_url, actions, is_feed_api, print_response_text)


if __name__ == '__main__':
    asyncio.run(main())


async def crawl_pdd():
    start_url = "https://mobile.yangkeduo.com/catgoods.html?refer_page_name=index&opt_id=1274&opt_name=T%E6%81%A4&opt_type=2"

    actions = []

    def scroll_down(amount: int, secs: int):
        async def _scroll_down(page: Page):
            start = time.time()
            while True:
                await page.evaluate("window.scrollBy({}, 0);".format(amount))
                await asyncio.sleep(2)
                if time.time() - start >= secs:
                    break

        return _scroll_down

    # 不断下滑 30 s
    actions.append(scroll_down(500, 60))

    async def print_response_text(res: Response):
        text = await res.text()
        print(text)

    await crawl_response(start_url, actions, lambda res: 'subfenlei_gyl_label' in res.url, print_response_text)


if __name__ == '__main__':
    asyncio.run(crawl_pdd())