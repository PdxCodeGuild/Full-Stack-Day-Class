# Practice: Pyramid
Save your solution as `pyramid.html` and `pyramid.css`.

Recreate the following layout using just flexbox.

* Each box should be a `div`
* Every box has a one pixel black border
* "Row" boxes should have 20 pixels of spacing between each other and between the page edges
* "Inner" boxes should have 10 pixels of spacing between themselves and the edge of the "row" box they are in
* Each "row" box should be 100 pixels high (including border) and the full width of the page (taking into account the above spacing)
* Each "inner" box should be the full height of the row (taking into account the above spacing)
* The first "row" box contains one "inner" box that is full width
* The second "row" box contains two "inner" boxes that fill out the full width between them in a 4:1 ratio
* The third "row" box contains three "inner" boxes that have content 20% the width of the "row" box and are spread out over the entire "row" box equally horizontally

The page edge is the grey outline.

<!-- This is not the correct way to do this. -->
<style>
.pyramid div {
    border: solid 1px black;
    position: absolute;
}
</style>
<div class="pyramid">
<div style="border: dashed 1px grey; width: 500px; height: 500px;">
    <div style="height: 98px; width: 460px; top: 20px; left: 20px;">
        <div style="height: 76px; width: 436px; top: 10px; left: 10px;"></div>
    </div>
    <div style="height: 98px; width: 460px; top: 140px; left: 20px;">
            <div style="height: 76px; width: 339px; top: 10px; left: 10px;"></div>
            <div style="height: 76px; width: 85px; top: 10px; right: 10px;"></div>
    </div>
    <div style="height: 98px; width: 460px; position: relative; top: 260px; left: 20px;">
        <div style="height: 76px; width: 90px; top: 10px; left: 10px;"></div>
        <div style="height: 76px; width: 90px; top: 10px; left: 184px;"></div>
        <div style="height: 76px; width: 90px; top: 10px; right: 10px;"></div>
    </div>
</div>
</div>
