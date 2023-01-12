//Canvas Objects

let cnv = document.getElementById("gameBoard");
let ctx = cnv.getContext("2d");
cnv.width = 600
cnv.height = 800
ctx.font = "30px Arial";

//Create Block
ctx.fillBlock = function (x1, y1, x2, y2, Color) {
    ctx.beginPath();
    ctx.rect(x1, y1, x2, y2);
    ctx.fillStyle = Color;
    ctx.fill();
}

//Create NoteBlocks
ctx.drawNoteBlocks = function (x1, y1, x2, y2, color) {
    ctx.beginPath();
    ctx.rect(x1, y1, x2, y2);
    ctx.fillStyle = color;
    ctx.fill();
}

//Create stroke
ctx.strokeBlock = function (x1, y1, x2, y2) {
    ctx.beginPath();
    ctx.rect(x1, y1, x2, y2);
    ctx.strokeStyle = "grey";
    ctx.stroke();
}

//Click Area Vals
function clickArea(fillXLocation, fillColor, strokeXLocation, keyBindNumber, keyBindXLocation) {
    ctx.fillBlock(fillXLocation, 650, 150, 70, fillColor)
    ctx.strokeBlock(strokeXLocation, 650, 150, 70)
    ctx.fillStyle = "black"
    ctx.fillText(keyBindNumber, keyBindXLocation, 695);

}