import baseball_reference_example as bfe

import pprint

def main():
    teams = bfe.BaseballReferenceCrawler().crawl()
    pprint.pprint(teams)


if __name__ == "__main__":
    main()
