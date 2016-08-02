# Web Inspector Style Basics

In the [web inspector](http://ruby.bastardsbook.com/chapters/web-inspecting-html/), when you select an element, the **style pane** will show you [the cascade](/notes/css-cascade.md) for that element.
Most specific rule sets will be at the top, least specific rule sets at the bottom.
Rules that are crossed out are overridden by more specific ones somewhere higher.
Rules with warning triangles are invalid.

## Modifications

You can live modify the CSS cascade using this pane.
Check and uncheck rules to temporarily enable or disable them.
Double click on text to edit it.

This is a great way to temporarily try out a change.

The modifications will not be saved in your CSS file.
They'll disappear on refresh.
You have to write the resulting rule sets in your file.
