import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pandas as pd
import random
import string
import time

os.environ["PATH"] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome(executable_path=r"C:/SeleniumDrivers/chromedriver.exe")
driver.implicitly_wait(20)

url_test = ["https://www.youtube.com/watch?v=Ww8A87xf0gU"]

url_list = [
    "https://www.youtube.com/watch?v=owGcH650Tfc",
    "https://www.youtube.com/watch?v=uegOUmgKB4E",
    "https://www.youtube.com/watch?v=BN88HPUm6j0",
    "https://www.youtube.com/watch?v=0ZsVxSDB7NY",
    "https://www.youtube.com/watch?v=qlClk9G15i4",
    "https://www.youtube.com/watch?v=f3lUEnMaiAU",
    "https://www.youtube.com/watch?v=c7iiz1sksLc",
    "https://www.youtube.com/watch?v=9e4AaXzagfc",
    "https://www.youtube.com/watch?v=SVk1hb0ZOrE",
    "https://www.youtube.com/watch?v=qzJkPIkAkEY",
    "https://www.youtube.com/watch?v=PPI6lte8mJs",
    "https://www.youtube.com/watch?v=FE4iFYqi4QU",
    "https://www.youtube.com/watch?v=A5U4lpFz92w",
    "https://www.youtube.com/watch?v=qsIbGKosY1E",
    "https://www.youtube.com/watch?v=fPsHN1KyRQ8",
    "https://www.youtube.com/watch?v=XHUCGNDoWp4",
    "https://www.youtube.com/watch?v=SqEo107j-uw",
    "https://www.youtube.com/watch?v=_LOPuClIrPo",
    "https://www.youtube.com/watch?v=MOXv7iR1AJk",
    "https://www.youtube.com/watch?v=ywPqLCc9zBU",
    "https://www.youtube.com/watch?v=E1QRlLCN4Gc",
    "https://www.youtube.com/watch?v=PeKqlDURpf8",
]

# Initialize list for the transcriptions to be stored as pandas dataframes
df_list = []

for video in url_list:
    driver.get(video)
    driver.maximize_window

    # Open ellipsis options
    for each in range(3):
        try:
            ellipsis = driver.find_element_by_xpath(
                '//yt-icon[@class="style-scope ytd-menu-renderer"]'
            )
            ellipsis.click()
            break
        except:
            driver.refresh()

    # Click and open the transcript box
    for each in range(3):
        try:
            try:
                open_transcript_button = driver.find_element_by_xpath(
                    '//ytd-menu-service-item-renderer[@class="style-scope ytd-menu-popup-renderer"]'
                )
                open_transcript_button.click()
            except:
                continue
            break
        except:
            driver.refresh()

    # Obtain timestamps and text data
    for each in range(3):
        try:
            transcript_timestamps = driver.find_elements_by_xpath(
                '//div[@class="cue-group-start-offset style-scope ytd-transcript-body-renderer"]'
            )
            break
        except:
            driver.refresh()

    for each in range(3):
        try:
            try:
                transcript_active_text = driver.find_element_by_xpath(
                    '//div[@class="cue style-scope ytd-transcript-body-renderer active"]'
                )
            except:
                pass
            break
        except:
            driver.refresh()

    for each in range(3):
        try:
            transcript_remaining_text = driver.find_elements_by_xpath(
                '//div[@class="cue style-scope ytd-transcript-body-renderer"]'
            )
            break
        except:
            driver.refresh()

    for each in range(3):
        try:
            video_title = [
                driver.find_element_by_xpath(
                    '//yt-formatted-string[@class="style-scope ytd-video-primary-info-renderer"]'
                ).text
            ] * len(transcript_timestamps)
            break
        except:
            driver.refresh()

    video_url = [video] * len(transcript_timestamps)

    billionaire = ["Elon Musk"] * len(transcript_timestamps)

    # Store all timestamps and text data into corresponding lists
    try:
        ttimestamps_list = []
        ttext_list = [transcript_active_text.text]
        for each in range(0, len(transcript_timestamps)):
            ttimestamps_list.append(transcript_timestamps[each].text)
            if each == len(transcript_timestamps) - 1:
                break
            ttext_list.append(transcript_remaining_text[each].text)
    except NameError:
        ttimestamps_list = []
        ttext_list = []
        for each in range(0, len(transcript_timestamps)):
            ttimestamps_list.append(transcript_timestamps[each].text)
            ttext_list.append(transcript_remaining_text[each].text)

    # Create transcription data that contains both timestamps and text
    t_data = list(
        zip(ttimestamps_list, ttext_list, video_title, video_url, billionaire)
    )

    # Add dataframe
    df = pd.DataFrame(
        t_data, columns=["timestamps", "text", "video_title", "url", "billionaire"]
    )

    # Save dataframe as csv file
    filepath = "C:/Users/Danie/OneDrive/Computer Science/billionaire_search_engine/files_not_yet_pushed_to_es/"
    csvname = billionaire[0] + "_" + video[-11:] + ".csv"
    filename = os.path.join(filepath, csvname)
    df.to_csv(filename, index=False, header=False)
