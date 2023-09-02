# buaa_auto_login

## 1. Git clone
```bash
git clone https://github.com/chenzt2020/buaa_auto_login.git
cd buaa_auto_login
```

## 2. Install selenium
```bash
sudo apt update
sudo apt install python3-pip
pip install selenium
```

## 3. Download webdriver from https://github.com/mozilla/geckodriver/releases and extract it to the working directory

## 4. Fill in the username and password and run by python
```bash
python3 buaa_auto_login.py
```

## 5. Configure scheduled tasks
```bash
crontab -e
*/10 * * * * cd /path/to/buaa_auto_login/ && python3 buaa_auto_login.py >> login.log
```