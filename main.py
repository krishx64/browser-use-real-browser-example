import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
	raise ValueError('GOOGLE_API_KEY is not set')

from browser_use import Agent, Browser, ChatGoogle, ChatOllama

# Connect to your existing Chrome browser
browser = Browser(
	# Windows path
    executable_path=r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    user_data_dir=r'C:\\Users\\jaisw\\AppData\\Local\\Google\\Chrome\\User Data',
	# MAC path
	# executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
	# user_data_dir='~/Library/Application Support/Google/Chrome',
    profile_directory="Default", #chrome profile
	dom_highlight_elements=True,
	# keep_alive= True, #turn on if don't want to close browser after a task
	# storage_state='./storage_state3.json' # if cookies not appear in the chrome session then enable this to use manual cookies inside the respective json
)


# NOTE: You have to close all Chrome browsers before running this example so that we can launch chrome in debug mode.
async def main():
	# save storage state
	agent = Agent(
		llm=ChatGoogle(model='gemini-2.5-flash-lite'), # set model
		# Google blocks this approach, so we use a different search engine
		task="open reddit.com and give me a list of 10 astrology subreddits",
		# use_vision=True, #whether to enable vision
		browser=browser,
	)
	await agent.run()
	# await browser.export_storage_state('storage_state3.json') #save cookies from current session


if __name__ == '__main__':
	asyncio.run(main())