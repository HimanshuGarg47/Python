1. Gather information about error
2. Reproduce error


*******It doesn't Work***********
If user tell it doesn't work. Then ask these question
    1. What were you trying to do?
    2. What steps did you follow?
    3. What was the expected result?
    4. What was the actual result?

When debugging problem, consider first asking simple questions?
Check that can you reproduce issue in your computer


********Creating a Reproduction Case*************8
Reproduction case - A way to verify if the problem is present or not

A reproduction case is a way to verify if a problem is present or not. It can be as simple as trying to login to a website and see the loading page, or as complex as trying to help a user with an application that won't start. The first step is to read the logs available to you, which will depend on the operating system and the application. When something isn't behaving as it should, look for an error message that will help you understand what's going on like unable to reach server, invalid file format, or permission denied. The next step is to isolate the conditions that trigger the issue, such as whether other users in the same office have experienced the problem, if the same user logs into a different computer, and if the applications config directory is moved away without deleting it. Having a clear reproduction case allows you to investigate the issue and quickly see what changes it, as well as share with others when asking for help.


***********Finding the root cause******************
When you first come across these concepts, it might seem that once you have a reproduction case, you already know the root cause of the problem. But more often than not, its not true. In our overloaded server example, we figured out that the backup system was blocking the websites from working, and so we mitigated that immediate problem to unblock the user. But we didnt really look into the root cause of our server being stuck. This could be because the network bandwidth is saturated, the disk transfer is too slow, the hard drive is faulty, or a bunch of other reasons. We also didnt do anything to make sure our backups could run successfully in the future. Understanding the root cause is essential for performing the long-term remediation. So how do we go about finding the actual root cause of the problem We generally follow a cycle of looking at the information we have, coming up with a hypothesis that could explain the problem, and then testing our hypothesis. If we confirm our theory, we found the root cause. If we dont, then we go back to the beginning and try different possibility. This is where our problem-solving creativity comes into play. We need to come up with an idea of a possible cause, check if its correct and if not, come up with a different idea until we find one that explains the problem. Our ideas dont come out of a void. To get inspired, we look at information we currently have and gather more if we need. Searching online for the error messages that we get or looking at the documentation of the applications involved can also help us imagine new possibilities of what might be at fault. Whenever possible, we should check our hypothesis in a test environment, instead of the production environment that our users are working with. That way, we avoid interfering with what our users are doing and we can tinker around without fear of breaking something important. Depending on what youre trying to fix, this might mean we have to try our code in a newly installed machine, spinning up a test server, using test data, and so on. It can take some time to get the setup, but the extra safety is definitely worth it. Even when it seems that the error might be related to the specific production environment, its always a good idea to check if we can reproduce the problem in a test environment before we modify production. In our overloaded server example, if the problem is with the hardware, we wouldnt be able to replicate it with a test server. In that case, we would need to either wait until the services arent being used or bring up a secondary server, migrate the services there, and only then look at whats wrong with the computer. On the flip side, if the problem is related to some configuration of either the web services or the backup service, wed still see it in the test server. So wed always start by setting up a test instance of the service and checking if the problem replicates there before touching the production instance.


*********Dealing with Intermittent Issues************
Have you ever tried to solve a problem that happened only occasionally Maybe youve dealt with programs that randomly crash, laptops that sometimes fail to suspend, web services that unexpectedly stop replying, or file contents that get corrupted.
But only in some cases, bugs that come and go are hard to reproduce, and are extremely annoying to debug.
If you work in IT, youve probably had your own dose of frustration while dealing with intermittent and issues.
So what can you do if youre trying to debug an issue like that The first step is to get more involved in whats going on, so that you understand when the issue happens and when it doesnt.
If youre dealing with a bug and a piece of code that you maintain, you can usually modify the program to log more information related to the problem.
Since you dont know exactly when the bug will trigger, you need to be thorough with the information that you log.
For example, I recently had an issue with the service IAM.
It was crashing sporadically, and I was at a loss trying to find out why.
Looking at the error message, I knew it had something to do with strings that use special characters, but I had no idea where the bug was exactly.
So I added more logging information to the service, around the inputs and the function calls that I suspect could be involved.
The next time the program crashed, I was able to identify the part of the code where I was missing the proper handling for the encoding, and fixed the problem.
If you cant modify the code of the program to get more information, check if theres a logging configuration that you can change.
Many applications and services already include a debugging mode that generates a lot more output then the default mode.
By enabling the debug information in advance, you can get a better picture of whats going on the next time the problem happens.
If thats not possible, youll need to resort to monitoring the environment when the issue triggers.
Depending on what the problem is, you might want to look at different sources of information, like the load on the computer, the processes running at the same time, the usage of the network, and so on.
For bugs that occur at random times, we need to repair our system to give us as much information as possible when the bug happens.
This might require several iterations until we get enough information to understand the issue, but dont lose hope.
Most of the time, you can finally get to the point where you can actually understand whats going on.



**************Intermittently Failing Script*************

A colleague recently developed a small application to send meeting reminders to people in the company, because someone kept forgetting to show up.
The sales team was the first to test the app last week, and it worked fine.
But this week, another user is trying to send a meeting reminder and the program keeps terminating with an error.
Since the colleague that developed the app is on the other side of the Atlantic, the user is asking for our help to figure out whats going on.
First, lets try running the program ourselves and check if we can reproduce the problem.
Were presented with a window where we can enter the date for the meeting, the title of the meeting, and the people that we want to send the reminder to.
The meeting reminder that the user was trying to send was for January 13th, and the title was Production Review.
As we are trying things out and dont want to be mailing reminders out with our tests, Ill set this one to send the reminders to meet.
It failed to send the email.
This means weve reproduced the issue.
Lets try reminder that the sales team sent last week which had worked fine.
In that case, the reminder had been sent for January 7th and the title was Sales All Hands.
Again, Ill send this to myself to avoid spanning people would test reminders.
Yes.
In this case, the program successfully sent the reminder.
Which parameter do you think is at fault The title or the date It could be either.
But Ill bet its the date.
Lets try it once more with January 13th as the date and Sales All Hands as the title.
Another failure.
So we have a reproduction case.
When we try to send the meeting reminder for January 13th, we get the failure message.
But if we try to send the same reminder for January 7th, it works fine.
Now, the next step is to find the root cause of the issue.
Why could our application work fine for January 7th but fail for January 13th There could be a bunch of reasons.
But in general, when dates are involved in a failure, the problem is due to how the dates are formatted.
In some countries, the dates are written with the month first and the day second.
While in other countries, its the other way around.
To figure out whats going on, lets add more debugging information to the program.
Well open the meetingreminder.
sh script, which is a script written in Bash.
We see that this script is calling a program called Zenity.
Zenity is the application showing the window to select the date, title, and emails.
The output generated by Zenity is stored in a variable called meetinginfo, which is then passed as a parameter to the sendreminders.
py, Python 3 script.
This script then sends the emails.
To get more information about the output generated by Zenity, wed like to see the value of the meetinginfo variable before the Python script gets called.
Lets add an echo statement to see that.
Lets save this and try again.
This time, well just use test as the meeting title, as we know the problem is with the date.