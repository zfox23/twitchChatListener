
/*
    `twitchChatListener.js`
    Copyright (c) 2020 Zach Fox

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
*/

// Change the value of this variable to the name of your Twitch channel.
const TWITCH_CHANNEL_NAME = "CHANGEME";

const CUSTOM_REWARD_ID_DICTIONARY = {
    // Replace this "CUSTOM_REWARD_ID_01" string with a Custom Reward ID.
    // It'll look something like:
    // "f0724737-07e7-4787-8bf8-241556c36359"
    "CUSTOM_REWARD_ID_01": {
        // This name is just for your convenience so you can remember what the reward is called.
        // This name isn't referenced elsewhere in the code.
        "name": "Custom Reward Name 01",
        // Change this to the function you want this script to call when someone redeems this reward.
        "action": customRewardAction01
    },
    // Follow the same instructions as above to add as many custom reward/action pairs as you want.
    "CUSTOM_REWARD_ID_02": {
        "name": "Custom Reward Name 02",
        "action": customRewardAction02
    }
};

// This is the function that will be called when "Custom Reward Action 01" is triggered.
function customRewardAction01() {
    console.log(`Custom Reward Action 01 Triggered!`);
    fetch('http://localhost:8088/?customRewardAction01', {
        mode: 'no-cors'
    }).then((response) => { })
        .catch((error) => { });
}

// This is the function that will be called when "Custom Reward Action 02" is triggered.
function customRewardAction02() {
    console.log(`Custom Reward Action 02 Triggered!`);
    fetch('http://localhost:8088/?customRewardAction02', {
        mode: 'no-cors'
    }).then((response) => { })
        .catch((error) => { });
}

ComfyJS.onChat = (user, message, flags, self, extra) => {
    // Uncomment this line of code if you need more debugging information about messages coming through your Twitch Chat.
    //console.log(`Got Chat!\nUser: ${user}\nMessage: ${message}\nFlags: ${JSON.stringify(flags)}\nSelf: ${self}\nExtra: ${JSON.stringify(extra)}`);

    // If we've received all of the information necessary to take action on a message we've received from Twitch Chat...
    if (flags && flags.customReward && extra && extra.customRewardId) {
        let rewardID = extra.customRewardId;

        console.log(`Someone redeemed a custom reward with ID: \`${rewardID}\`.\nTheir chat message was: "${message}"`);

        if (!CUSTOM_REWARD_ID_DICTIONARY[rewardID]) {
            console.error(`There is no reward associated with the Custom Reward ID \`${rewardID}\``);
            return;
        }

        if (!CUSTOM_REWARD_ID_DICTIONARY[rewardID].action) {
            console.error(`There is no action associated with the Custom Reward ID \`${rewardID}\``);
            return;
        }

        CUSTOM_REWARD_ID_DICTIONARY[rewardID].action();
    }
}

ComfyJS.Init(TWITCH_CHANNEL_NAME);