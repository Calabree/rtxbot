
# Card Bot

**Description**: this is a bot written in python in an attempt to get more cards in the hands of everyday users.(US Only) 
***NOTE***: *THIS WILL NOT AUTO BUY, THIS IS FOR ALERT USE ONLY!*

**Currently Working:**
- Best Buy
**Currently Not Working:**
- NewEgg
- Amazon
- Stopping reoccurring emails on in stock products that you have been alerted on already. 

**Planned for next release**:
- Making sure you are not re-alerted for the exact same item multiple times within the same stock period.
- Code overhaul to make the source code much easier to read and much more modular.
## How To Get Up and Running 
**Step 1:**  Clone this project to your desired directory. 
**Step 2:** Navigate to that directory and run the following:
```python
#It is recommended that you run this in a virtual enviornment,
pip install -r requirements.txt
```
**Step 3:** Create a Best Buy developer account, and obtain an API key from them
**Step 4:** Make a new (or use your current one) Gmail. We will use this Gmail to notify you via email/text.
YOU WILL NEED TO ALLOW LESS SECURE APPS. [FOLLOW THIS LINK](https://support.google.com/accounts/answer/6010255?hl=en)
This is why I recommend you use a separate email account from your own.
**Step 5:** Fill out the *config_example.ini* and rename to **config.ini**
```ini
[COMMON]
APIKEY = <this is the bestbuy api key>
EMAILADDRESS = <the email address you are using to notify you of instock cards>
EMAILPW =<password to the above email address>
NOTIFYCONTACT=<the number you want to text>
```
When texting from an email you need to use the handle correspondent to your cell service provider. The are as follows:
**Verizon Wireless**: @vtext.com
**AT&T**: @txt.att.net
**T-Mobile**: @tmomail.net
Inside BestBuyScan.py, look for the following text commend
```python
#Replace Code Here
```
and replace the message variable with the following:
```python
message = f"""\
Subject: CARD FOUND
Card: {w[c].json()["products"][j]["name"]}
URL: {w[c].json()["products"][j]["url"]}"""
```
**NOTE**: MAKE SURE YOU FOLLOW THE SAME FORMATTING, OTHERWISE EMAIL WILL NOT PROPERLY SEND. THIS WILL BE FIXED IN THE NEXT RELEASE!