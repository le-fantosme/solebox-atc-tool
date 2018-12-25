# solebox-atc-tool
A short Python script to auto add to cart and checkout selected item in few seconds.

How to use:

1. clone the repository on your machine
2. install the requirements
3. run the whole script
4. create an account on solebox in your standard browser and add your shipping/billing addrress in the account. When running the script you must contemporary be logged in on the solebox website in your browser. I recommend, around 5 minutes before the "release", log in on website and start the script.

Edit all the code parts marked with comments by inserting your data.
Enter the item link in productlink. To get the aid value, inspect a size and you will see a number like this: a#NUMBER.selectsize in the right corner. The Number is your aid value you can enter in the script's source code.

The script doesn't support Solebox's Queue release methods obviously. I might publish that later.

For any major problems open an issue. If you want, create a pull request.

For any exact explanations of the script, I am publishing a tutorial on my YT (here you find part 1 https://youtu.be/mOPoPu7dc4o )

Obviously the script is work in progress. I am not publishing my top Solebox Script obviously, this is just a smallsmall proof of concept. Still I will add some features soon of course if I am in the correct mood of working:
TODOs:
- Queue bypass
- Restock mode and restock monitor
- Stock checker
- Scheduled tasks (start at specific time)
- Multi threaded script (tasks)
- Auto size selection (no more AID value needed)
- Proxy support
- Webhook output
- Make it generally more stable and fast

