from GetPage import get_page
import re
def get_all_links(page):
	links = []
	while True:
		url,endpos = get_next_target(page)
		if url:
			if url not in links:
				links.append(url)
			page = page[endpos:]
        	else:
           		 break
	return links

def get_next_target(page):

    page=re.sub(r'<!--(.*?)-->', '', page)
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

#L2 = get_all_links(get_page("http://www.mmw.net63.net"))
#for r in L2:
	#print r+"\n"





	
