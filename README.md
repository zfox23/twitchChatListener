# Twitch Chat Listener
`Twitch Chat Listener` is a set of scripts you can customize and use to trigger various actions on your stream or in your game based on what people are doing in your Twitch chat, including emulating keyboard input when someone redeems channel points.

I made this set of scripts for [CrispyTaytorTot](https://twitch.tv/crispytaytortot) so that, when someone redemeed channel points in his chat for the "Boost" reward, his Elite Dangerous ship would boost uncontrollably, causing many laughs and entertaining many people. Maybe that will inspire you!

# How do I set this up?
Buckle up - there are a lot of steps here. I've tried to be explicit as possible so that everyone can follow along.

## Step 01: Install Prerequisite Software
1. Clone this repository, or download and unzip this repository's code to your hard drive.
2. Install the latest version of [Python](https://www.python.org/) on your machine, ensuring its installation path is added to your `PATH` environment variable.
    - I'm using [Python 3.8.2 x64 for Windows](https://www.python.org/ftp/python/3.8.2/python-3.8.2-amd64.exe).
3. Open a Command Prompt/PowerShell/Terminal instance and `cd` into the directory where `Twitch Chat Listener` is stored on your hard drive.
4. `cd` into the `python` subdirectory.
5. Run `pip install -r requirements.txt` to install this software's Python dependencies.
    - `Twitch Chat Listener` depends on:
        - [pynput](https://pypi.org/project/pynput/)

## Step 02: Configure Twitch
Next, you'll need to configure your Twitch channel so that people can redeem Channel Points for **custom rewards**.
[Follow this helpful guide on Twitch's website to do this.](https://help.twitch.tv/s/article/channel-points-guide?language=en_US#streamer)
**When you do this, you MUST check the box that says "Require Viewer to Enter Text".** If you don't do this, the scripts won't be able to recognize your custom rewards!

## Step 03: Figure Out the Custom Reward IDs of Your Custom Rewards
Now, you have to figure out the Custom Reward ID strings associated with the custom rewards you set up above.

1. Open `<twitchChatListener Repo Directory>\web\twitchChatListener.js` in your favorite text editor.
2. Look toward the top of the file for `const TWITCH_CHANNEL_NAME = "CHANGEME";`. Change `"CHANGEME"` to the name of your Twitch channel.
    - For me, I would change `"CHANGEME"` to `"Valefox"`.
3. Open a Command Prompt/PowerShell/Terminal instance and `cd` into the directory where `Twitch Chat Listener` is stored on your hard drive.
4. `cd` into the `web` subdirectory.
5. Run `python -m http.server 80` to start a simple HTTP server that will serve the HTML portion of this software.
6. Open your Web browser to [`http://localhost`](http://localhost).
7. Open your browser's developer console.
    - I use Firefox. For me, I do this by pressing `F12` on my keyboard. Your browser may be different, but it's probably also `F12` for you.
8. You should see `Connected:irc-ws.chat.twitch.tv:443` in the console.
9. In a different browser window, or on your phone, redeem a custom channel reward with your unlimited channel points.
10. In your browser's developer console, you should now see something like:
    ```
    Someone redeemed a custom reward with ID: `<Custom Reward ID>`.
    Their chat message was: "<the message you entered when redeeming the reward>"
    There is no reward associated with the Custom Reward ID `<Custom Reward ID>`
    ```
11. Open `<twitchChatListener Repo Directory>\web\twitchChatListener.js` in your favorite text editor.
12. Inside the definition of `CUSTOM_REWARD_ID_DICTIONARY`, you'll see `CUSTOM_REWARD_ID_01`. Replace `CUSTOM_REWARD_ID_01` with the `<Custom Reward ID>` that you saw in the developer console above.
13. Change `Custom Reward Name 01` to some name you can remember.
14. You don't have to change anything else here if you don't want to. If you know what you're doing, you may want to change some other things in here 😊. If not, save and close `twitchChatListener.js`.

## Step 04: Refresh the Webpage
Now that you've made necessary changes to the JavaScript code, you need to hard-refresh the browser tab you have pointed at `http://localhost` so that your browser tab sees those changes. You can press `CTRL+F5` to hard-refresh, which will clear any cache your browser has of the page.

## Step 05: Modify `listenerPythonServer.py`
Next, we need to set up `listenerPythonServer.py`, which will interpret HTTP requests made by `twitchChatListener.js` when someone redeems a Custom Reward on your channel. At that point, you can make the Python script do things like emulate keyboard keypresses - or, really, do anything that Python can do!
1. Open `<twitchChatListener Repo Directory>\python\listenerPythonServer.py` in your favorite text editor. This file is heavily commented, so you might not need any more instructions...
2. Modify the definition of the function `customRewardAction01()` to do whatever you want it to do. In the example case, when a user redeems Custom Reward 01, the keyboard combination `LEFT ALT + RIGHT ALT + E` will be pressed and then released!
3. In this example, code, you can see this code:
    ```
    elif query == 'customRewardAction02':
        # As an example, we show what code looks like if we want to defer an action for five seconds.
        print('Calling `customRewardAction02()` in 5.0 seconds.')
        timer = threading.Timer(5.0, customRewardAction02)
        timer.start()
    ```
This example code shows how you can defer a custom reward action for five seconds.

## Step 06: Get Creative!
At this point, the only limit to what you can do with these scripts is your imagination!
You could, for example:
- Modify `twitchChatListener.js` so that, when someone redeems a reward, the JS modifies the `index.html` DOM to show a graphic for 5 seconds. You could then set `index.html` as a Web Source within OBS.
- Modify `twitchChatListener.js` so that it can respond to chat messages generically instead of only listening for Custom Reward Redemptions.
- Modify `listenerPythonServer.py` to interface with Smart Bulbs in your home to change the color of your room lights if someone redeems a reward.

## Step 07: Start it up!
Read on below to learn how to get everything running once you have set up your environment.

# Great! I set everything up. Now **how do I get this thing running?**
The steps below assume that none of the scripts in this repository are currently running. You can kill any Python HTTP Server that is running by pressing `CTRL+C` in the Python terminal window.

**To enable Twitch Chat Listener and enable custom Channel Reward Redemption Actions:**
1. Open a Command Prompt/PowerShell/Terminal instance and `cd` into the directory where `Twitch Chat Listener` is stored on your hard drive.
2. `cd` into the `web` subdirectory.
3. Run `python -m http.server 80` to start a simple HTTP server that will serve the HTML portion of this software.
4. Open your Web browser to [`http://localhost`](http://localhost).
5. Open a Command Prompt/PowerShell/Terminal instance and `cd` into the directory where `Twitch Chat Listener` is stored on your hard drive.
6. `cd` into the `python` subdirectory.
7. Run `python .\listenerPythonServer.py`.

# Credits?
`Twitch Chat Listener` makes use of [Instafluff's `ComfyJS`](https://github.com/instafluff/ComfyJS), a fantastic piece of software that "lets you integrate with Twitch chat for your Twitch channel SUPER EASILY in just a few lines of code". Thanks, Instafluff!