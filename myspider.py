import scrapy
import json
import base64
import requests


def write_results_file(marcas):
    marcas_ordenadas = sorted(marcas, key=lambda d: d['name'])
    jsonstring = json.dumps(marcas_ordenadas)
    jsonfile = open('marcas.json', 'w')
    jsonfile.write(jsonstring)
    jsonfile.close()


def urls_brands():
    base_url = 'https://www.rankingthebrands.com/The-Brands-and-their-Rankings.aspx?catFilter=0&nameFilter='
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'
    urls = list()
    for l in alfabeto:
        urls.append(base_url + l)
    return urls


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = urls_brands()
    home_url = 'https://www.rankingthebrands.com/'
    marcas = list()

    def parse(self, response):
        for link in response.css('.brandLine a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_details)

    def parse_details(self, response):
        brandName = response.css('.brandName span::text').get()
        brandLogo = self.home_url + str(response.css('.brandLogo img::attr(src)').get())
        gbin = response.css('.brandInfoText span::text').get()

        urlToBytes = str(requests.get(brandLogo).content).encode("ascii")
        imgBase64 = str(base64.b64encode(urlToBytes))

        country = response.css('.brandInfoText span::text')[2].get()
        rtbScore = response.css('.brandInfoText span::text')[1].get()

        yield {
            'name': brandName,
            'logo': brandLogo,
            'gbin': gbin,
            'base64': imgBase64,
            'country': country,
            'score': rtbScore
        }

        self.marcas.append({'name': brandName, 'logo': brandLogo, "gbin": gbin, 'base64': imgBase64, 'country': country, 'score': rtbScore})
        write_results_file(self.marcas)


    def close(self, reason):
        print("SCRAPY FINALIZOU!")
