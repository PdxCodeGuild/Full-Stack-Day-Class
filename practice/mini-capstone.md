# Practice: Mini Capstone

In groups of about three, you'll be working on a larger project for the next few days.

## 1. Brainstorm Idea

Together, brainstorm an idea for what you want your project to do.

**At the beginning, there are no bad ideas!**
Literally write a super short version of every idea down on the whiteboard.
Keep building upon existing ideas.
_Don't_ flesh them out; keep expanding and saying "yes" and going places.
Nothing is too hard to complete yet.

Do this for ~20 minutes.
Then, take a break.

### Hints

*   What do you wish your computer did for you?

*   What's a problem you've had in the last few weeks that was very manual and a computer could automate?

*   What's a game you like to play or activity you participate in?
    Is there a way you could make it more convenient or recreate it?

## 2. Reality Check

When you come back from break, pick two or three ideas that excite you most.

I'm sure all three of your best ideas are awesome.
But you might not be able to complete an implementation of all of them in a few days.

Bring your ideas to me, and I'll vet and hone them with you into something that is doable in about a week.
We will prioritize the most core features and make an [MVP](/notes/capstone-mvp.md) and name your project.

## 3. Divide and Conquer

Now that we have the features of your project, we need to divvy up work on it.
I'll identify some big **moving parts** in your project and together we'll decide who will work on each big part.

I'm going to make a [Trello board](https://trello.com) for each Mini Capstone assignment and invite you to it.
It's a super lightweight way to keep track of tasks.

I'll make all of the starter tasks for all the moving parts.
Your team should make individual tasks for any sub-parts.
You should move tasks through the pipeline on your own!

Don't worry about following any formal task format or protocol.

## 4. Setup Logistics

1. [Make a new GitHub repo](https://github.com/new) named after your project.
1. Add your partners GitHub accounts as **collaborators** for that repo under `Settings -> Collaborators`.
1. Clone that repo on one computer.
1. On that computer, work together mirroring the [Python application structure](/notes/py-app-structure.md).
1. Make a trivial `hello.py` with a "hello world" in it that runs in the application's virtualenv through PyCharm.
1. Commit the whole application and push it to `master`.

## 5. Go

Now that work has been divvied up and the initial source template made, work starts independently.
Pick a chunk of the work assigned to you.

Then follow basically the [Git branching workflow](/notes/git-workflow-branching.md):

1.  Make a branch off `master`.

1.  Do work!
    Commit your work to that branch until that chunk of work is done.

1.  Push it to `origin`.

1.  Make a Pull Request.

1.  Have your partners and me **code review** your request.
    If you like the code and think it is worthy of merging into `master` so everyone sees it, comment on the Pull Request with "Ship It!".

1.  Once everyone has "Ship It!"ed, merge your Pull Request.

1.  Repeat.

**Work on your MVP features first and only work on other features once you're done.**
I cannot stress how important it is to do this.
We have a limited amount of time to work on this, and it's really satisfying to have something functional.
If you dive too deep on one task, your group might not finish.

You can still work on all the deep cool stuff later!

## 6. Readme

Ensure that your mini-capstone repo has a `readme.md` that describes:

1. A high-level description of what the project does
1. How someone could clone and run it themselves
1. Any future work
