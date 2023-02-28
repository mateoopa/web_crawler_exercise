from selenium.webdriver.common.by import By
import module
import json
import validators
import traceback
import sys


class WebCrawler:

    def __init__(self):
        self.parameters = module.GetParam()
        self.bot = module.Selenium()
        self.results = None

    def get_images(self):
        self.bot.navigate(self.parameters.start_url, True)
        img_xpath = '//descendant::img[1]'
        links_xpath = '//a[@href and not(@disabled)]'

        links = self.bot.fe(multiple=True, by=By.XPATH, elements=links_xpath, stop=True)
        all_links = [self.parameters.start_url]
        results = []

        if self.parameters.depth > len(links):
            print(f'Depth number exceeded. Links available for {self.parameters.start_url} are {len(links)}')
            self.bot.quit_driver()
            sys.exit(0)

        for counter, link in enumerate(links, 1):
            try:
                if counter > self.parameters.depth:
                    break
                else:
                    current_link = link.get_attribute('href')
                    if current_link not in all_links:
                        all_links.append(current_link)
                    else:
                        self.parameters.depth = self.parameters.depth + 1
                        continue
            except (Exception,):
                print(f'{traceback.format_exc()} {locals()}')
                continue

        for counter, link in enumerate(all_links, 0):

            if validators.url(link):
                self.bot.navigate(link, True)
                images = self.bot.fe(multiple=True, by=By.XPATH, elements=img_xpath, stop=False)

                if not images:
                    continue
                for image in images:
                    try:
                        if not image.get_attribute('src'):
                            continue
                        my_dict = {'imageUrl': image.get_attribute('src'),
                                   'sourceUrl': self.bot.driver.current_url,
                                   'depth': counter}
                        results.append(my_dict)
                    except (Exception,):
                        continue
        self.bot.quit_driver()
        self.results = {"results": [results]}

    def save_json(self):
        json_object = json.dumps(self.results, indent=4)

        with open("results.json", "w") as outfile:
            outfile.write(json_object)


crawler = WebCrawler()
crawler.get_images()
crawler.save_json()

