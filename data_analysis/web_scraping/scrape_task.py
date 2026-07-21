#!/usr/bin/env python3
"""scraping the page of a project to save it in a md for learning puproses"""

from bs4 import BeautifulSoup
import time
from selenium import webdriver
import json

"""
----
PLEASE ADJUST URL, USER, PWD
----
"""

# url to project
project_url = "https://intranet-dlh.hbtn.io/projects/3699"
# your user id
user = ""
# your pwd
pwd = ''


"""
---
SCRAPING Happening
---
"""

login_url = "https://intranet-dlh.hbtn.io/auth/sign_in"


# 1. Initialize the browser driver (This opens a visible Chrome window)
print("Opening browser...")

browser_options = webdriver.ChromeOptions()
#browser_options.add_argument("--headless")
# define 1920 1080 window
# browser_options.add_argument("--window-size=1920,1080")
browser_options.add_argument("--no-sandbox")
# prevents memory crashes
browser_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=browser_options)

try:
    # 2. Go to the login page
    driver.get(login_url)

    # 3. Pause the script to let you manually log in via Google/Microsoft
    print("\n" + "="*50)
    print("ACTION REQUIRED: Please use the opened Chrome window to log in.")
    print("Once you are successfully logged into the intranet dashboard,")
    print("come back to this terminal and press ENTER to continue script execution.")
    print("="*50 + "\n")
    
    input("Press ENTER here once you have finished logging in...")

    # 4. Use the authenticated browser session to visit the project page
    print(f"Navigating to project page: {project_url}")
    driver.get(project_url)
    
    # Give the page a couple of seconds to load completely
    time.sleep(3)
    
    # 5. Extract the HTML source and pass it over to BeautifulSoup
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, "html.parser")
    title = soup.title.text.strip()
    
    # print("Project Page Title:", soup.title.text.strip())
    x = title.find('|') -1
    y = title.find(': ') +2
    # print(f"title: {tit_md}")
    if y > 1 and x > 0:
        tit_md = title[y:x].strip()
    else:
        # Fallback filename if the title layout is missing characters
        tit_md = "Project_Notes"


    # 6 Let the Scrapping begin:
    mdfile = tit_md + ".md"
    print(f"Creating file: {mdfile}")
    
    #6a: Title
    with open (mdfile, "w", encoding="utf-8") as f:
        f.write("# " + title + "\n\n")
    
    #6b resources, learning objectives and requirements
    base_url = "https://intranet-dlh.hbtn.io/"

    resources_head = soup.find("h2", id="resources")

    if resources_head:
        # find very next <ul> sibling element
        markdown_links = []
        markdown_links.append("## Resources\n")
        
        current_element = resources_head.find_next_sibling()
        while current_element and current_element.name != "h2":
            # paragraphs
            if current_element.name == "p":
                p_text = current_element.text.strip()
                if p_text:
                    markdown_links.append(f"\n**{p_text}**\n")
            # links
            elif current_element.name =="ul":
                for link in current_element.find_all("a"):
                    link_text = link.text.strip()
                    relative_href = link.get("href", "")
                
                    if relative_href.startswith("/"):
                        full_url = base_url + relative_href
                    else:
                        full_url = relative_href
            
                    markdown_links.append(f"* [{link_text}]({full_url})")

            current_element = current_element.find_next_sibling()

        resources_markdown = "\n".join(markdown_links)

        with open(mdfile, "a", encoding="utf-8") as f:
            f.write(resources_markdown)

        print("successfully appended resource")
    
    # 7 Learning Objectives
    lo_head = soup.find("h2", id="learningobjectives")
    if lo_head:
        # find very next <ul> sibling element
        markdown = []
        markdown.append("\n\n## Learning Objectives\n")
        
        current_element = lo_head.find_next_sibling()
        while current_element and current_element.name != "h2":
            # if li is a sibling
            if current_element.name == "li":
                li_text = current_element.text.strip()
                if li_text:
                    markdown.append(f"\n* {li_text}")
            # if li is a child 
            else:
                for li in current_element.find_all("li"):
                    li_text = li.text.strip()
                    if li_text:
                        markdown.append(f"* {li_text}")
            
            current_element = current_element.find_next_sibling()

        lo_markdown = "\n".join(markdown)

        with open(mdfile, "a", encoding="utf-8") as f:
            f.write(lo_markdown)  

        print("successfully appended learning objectives") 

    # Tasks
    task_head = "\n\n---\n\n## TASKS\n\n"

    with open(mdfile, "a", encoding="utf-8") as f:
        f.write(task_head)

    
    # loop over all panels
    all_tasks = soup.find_all("div", class_="task-container")
    task_list = []


    for task in all_tasks:
        # title parsing
        task_head = task.find("h3") or task.find(class_="panel_title")

        if task_head:
                task_head_text = task_head.text.strip()
        else:
            position = task.get("data_position", "Unkown")
            task_head_text = f"Task {position}"
                    
        task_list.append(f"**{task_head_text}**\n")
        
        # extract description

        task_desc = task.find("div", class_="task-description-markdown") or task.find(class_="panel_body")

        if task_desc:
            task_desc_text = task_desc.text.strip()
            task_list.append(f"{task_desc_text}\n\n")
        else: 
            task_list.append(f"*No description found for this task.*\n\n")

    # create a text string block
    task_markdown = "\n".join(task_list)

    with open(mdfile, "a", encoding="utf-8") as f:
        f.write(task_markdown)
    
    print(f"successfully appended all {len(all_tasks)} tasks")

finally:
    print("Closing browser...")
    driver.quit()
