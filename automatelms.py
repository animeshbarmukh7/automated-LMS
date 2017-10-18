from selenium import webdriver as wb
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv


visitedLinks=set()
file=open('lms.csv','r')
reader=csv.reader(file,delimiter=',')
for row in reader:
    user=row[0]
    passw=row[1]


       
driver=wb.Chrome(r'''C:\Users\admin\Downloads\chromedriver.exe''')
driver.maximize_window()
page=driver.get("http://mydy.dypatil.edu/")
wait = WebDriverWait(driver, 15)
#print(user+'   '+passw)
driver.find_element_by_name("username").send_keys(user)
driver.find_element_by_name("next").send_keys(Keys.ENTER)
driver.find_element_by_name("password").send_keys(passw)
driver.find_element_by_id("loginbtn").send_keys(Keys.ENTER)




#driver.find_element_by_class_name("launchbutton").send_keys(Keys.CONTROL+Keys.ENTER)
#time.sleep(5)
#lists=driver.find_element_by_class_name("launchbutton")
#print(driver.page_source)
#soup=bs(driver.page_source,'html.parser')
#maintext=soup.find_all('td')
#print(maintext)
        
#maintext=soup.find_all('td',{'class':'cell c3 lastcol'})
#print(maintext)

#like = driver.find_elements_by_class_name('launchbutton')
#for x in range(0,len(like)):
    #if like[x].is_displayed():
 #   like[x].click()





def forumButton():
    
    driver.find_element_by_xpath("//*[@value='Add a new discussion topic']").send_keys(Keys.ENTER)
    wait.until(EC.presence_of_element_located((By.ID ,"id_subject"))).send_keys('Why Django?')
    wait.until(EC.presence_of_element_located((By.ID ,"id_messageeditable"))).send_keys('cause Django is best')

    

def openurl():
    for i in range(len(driver.window_handles)-1):
        driver.switch_to_window(driver.window_handles[1])
       # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+Keys.PAGE_UP)
        url = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT ,"https://www")))
        url.click()
        time.sleep(0.2)
        driver.close()
        driver.switch_to_window(driver.window_handles[0])


def tryurl():
    driver.switch_to_window(driver.window_handles[2])
    url = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT ,"://")))
    url.click()
    time.sleep(0.5)
    driver.close()
    driver.switch_to_window(driver.window_handles[1])
 
        

def openpage(te):
    time.sleep(1)
    i=0
    try:
        links=wait.until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT,te)))
        for x in range(0,len(links)):
            if links[x].is_displayed():
                links[x].send_keys(Keys.CONTROL+Keys.ENTER)
                #print('\n Links Called'+str(i))
                i+=1
                tryurl()
    except TimeoutException:
        print("Exception has been thrown ")

        
  
    
def getAllLinks():
    
    search = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME ,"inner_activities")))
    return search
    
def opend():
    driver.get('http://mydy.dypatil.edu/rait/course/view.php?id=860')
    time.sleep(1)
    #driver.find_element_by_link_text('Discussion forum').click()
    wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,'Discussion forum'))).click()
    wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'DF-1'))).send_keys(Keys.CONTROL+Keys.ENTER)
    driver.switch_to_window(driver.window_handles[1])
    forumButton()
    



def isinset(a):
    print(visitedLinks)
    print('\n')
    return (a in visitedLinks)
            
def readmaterial():
    driver.find_element_by_link_text('Reading material').click()
    search=getAllLinks()
    for item in search:
        output=str(item.text)
        text=''.join(output)
        newtext=text.splitlines()
        for te in newtext:
            flag=isinset(te)
            if flag==False:
                visitedLinks.add(te)
                openpage(te)
            
    #openpage(newtext[0])
    #openurl()

    
def launch():
    links=driver.find_elements_by_class_name('launchbutton')
    for x in range(0,len(links)):
        links[x].send_keys(Keys.CONTROL+Keys.ENTER)
        driver.switch_to_window(driver.window_handles[1])
        visitedLinks.clear()
        readmaterial()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])

launch()





#driver.get('http://mydy.dypatil.edu/rait/course/view.php?id=860')
#readmaterial()
#opend()
                                                   
#driver.implicitly_wait(5)
#links=driver.find_element_by_xpath('//*[@href]')
#print(links.get_attribute('href'))

#soup=bs(driver.page_source,'html.parser')
#maintext=[]
#maintext=soup.find_all('ul',{'class':'gridicons'})

#links=[]
#print(maintext)
#print('\n\n')
#for link in maintext:
    #te=link.find_all('a')
   # print(str(te)+ "\n")
    #for ele in te:
        #links.append(ele.get_attribute('href'))
        #print(str(ele)+"    ")
#print(links)


