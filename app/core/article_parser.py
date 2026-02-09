from bs4 import BeautifulSoup
#FUNCTION - ArticleParser is responsible for parsing the rendered HTML content to extract article information such as title, author, publication date, and main content. It uses BeautifulSoup to navigate the HTML structure and identify relevant elements based on tags and classes. The parser returns structured data that can be easily stored in a database or used for further processing. It also handles edge cases where certain information may be missing or formatted differently across websites, ensuring that the parsing logic is adaptable to different website structures and can be easily updated as needed.
class ArticleParser:
    """
    Responsible for -
    -Parsing rendered HTML content to extract article information such as title, author, publication date, and main content.
     -Using BeautifulSoup to navigate the HTML structure and identify relevant elements based on tags and classes.
     -Returning structured data that can be easily stored in a database or used for further processing.
     -Handling edge cases where certain information may be missing or formatted differently across websites.
     -Ensuring that the parsing logic is adaptable to different website structures and can be easily updated as needed.
    """
    def parse(self,html: str)-> list[dict]: #returns a list of articles, where each article is represented as a dictionary containing the extracted information.
        soup = BeautifulSoup(html, "html.parser")

        articles = [] # Initialize an empty list to store the extracted articles

        rows = soup.find_all("tr",class_="athing") # Find all <tr> elements with the class "athing", which represent individual articles on Hacker News

        for row in rows:
            title_tag = row.find("span", class_="titleline") # Within each article row, find the <span> element with the class "titleline", which contains the article title and link
            link_tag = title_tag.find("a") if title_tag else None # From the titleline, find the <a> tag which contains the article URL. If title_tag is None, link_tag will also be None

            if not link_tag: # If there is no link tag, skip this article and move to the next one
                continue
            # Extract the article information and store it in a dictionary
            article ={
                "title": link_tag.get_text(strip= True),
                "url": link_tag.get("href"),
                "source": "news.ycombinator.com"
            }

            articles.append(article)
        return articles


