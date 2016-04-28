# Miran
A static blog and static site generator, written in python, easy to build upon!

##How it works
- You write a post  using the miranmarkup
- Miran converts the post into html and creates a new file combining the template.html and the converted html!
- Miran adds the post to the index page.

##Formatting
      :t: Title :t: - Title

      :d: - date

      :p: Example text :p: - new paragraph

      :b: bold : b :

      :i: italic :i: 

You can also add new "commands" by opening miran.py and in the add-on pasting this:


    while ":letter:" in text:

    text = str(text);
    
    text = text.replace(":letter:","<letter>",1);
    
    text = text.replace(":letter:","</letter>",1); 
    
-- ofc by replacing the letter with a s , for example, which will get you strikethrough 


You can also just write plain html like:
`<b>This will be bold</b>`(<b>This will be bold</b>)
`<a href="https://github.com">click me</a>`(<a href="https://github.com">click me</a>)
and so on.
