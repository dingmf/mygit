import scrapy.cmdline

def main():
    scrapy.cmdline.execute(['scrapy', 'crawl', 'mysina'])

if __name__ == '__main__':
    main()