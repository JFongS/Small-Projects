//Osu Mania Unlimited

//Event Listeners
document.addEventListener('keydown', keyPressed)

//Global Variables
let noteBlocks = [];

//Establish click area
let area1 = ""
let area2 = ""
let area3 = ""
let area4 = ""
//Establish key letters
let keyBind1 = "D"
let keyBind2 = "F"
let keyBind3 = "J"
let keyBind4 = "K"

let color = ["yellow", "pink", "yellow", "white"]

//Variables for game
let speed = 10
let score = 0
let misses = 0

let startGame = false
let endGame = false

// Main Program Loop
requestAnimationFrame(draw);

function draw() {
    // Logic

    // Drawing
    ctx.clearRect(0, 0, cnv.width, cnv.height);

    //Clicking Area letter for each block
    area1 = clickArea(0, "yellow", 0, keyBind1, 65)
    area2 = clickArea(150, "pink", 150, keyBind2, 215)
    area3 = clickArea(300, "yellow", 300, keyBind3, 360)
    area4 = clickArea(450, "white", 450, keyBind4, 515)


    //Draw Noteblocks 
    for (let i = 0; i < noteBlocks.length; i++) {
        ctx.drawNoteBlocks(noteBlocks[i].xLocation, noteBlocks[i].yLocation, noteBlocks[i].x, noteBlocks[i].y, randomSetColor(i))
    }
    //Set the game start Screen
    if (startGame == false) {
        ctx.fillStyle = "white"
        ctx.font = "25px Arial"
        ctx.fillText("Press 's' to start the game!", 150, 250)

        clearInterval(falling);
    }




    //Set the game end screen
    if (endGame == true) {
        ctx.fillStyle = "white"
        ctx.font = "25px Arial"
        ctx.fillText("You got 50 misses! Press 'r' to play again", 75, 250)
    }

    // Request another Animation Frame
    requestAnimationFrame(draw);
}


// Helper Functions

//When the key is being Pressed
function keyPressed() {

    //Keys needed for game 

    //Key D is pressed
    if (event.code == 'KeyD') {
        keyBind1 = ""
        for (let i = 0; i < noteBlocks.length; i++) {
            if (noteBlocks[i].yLocation < 690 && noteBlocks[i].yLocation > 580 && noteBlocks[i].xLocation == 0) {
                noteBlocks.splice(i, 1)
                score++
                document.getElementById("score").innerHTML = score
            }
        }

    }

    //Key F is pressed
    else if (event.code == 'KeyF') {
        keyBind2 = ""
        for (let i = 0; i < noteBlocks.length; i++) {
            if (noteBlocks[i].yLocation < 690 && noteBlocks[i].yLocation > 580 && noteBlocks[i].xLocation == 150) {
                noteBlocks.splice(i, 1)
                score++
                document.getElementById("score").innerHTML = score
            }
        }

    }

    //Key J is pressed
    else if (event.code == 'KeyJ') {
        keyBind3 = ""
        for (let i = 0; i < noteBlocks.length; i++) {
            if (noteBlocks[i].yLocation < 690 && noteBlocks[i].yLocation > 580 && noteBlocks[i].xLocation == 300) {
                noteBlocks.splice(i, 1)
                score++
                document.getElementById("score").innerHTML = score
            }
        }

    }

    //Key K is pressed
    else if (event.code == 'KeyK') {
        keyBind4 = ""
        for (let i = 0; i < noteBlocks.length; i++) {
            if (noteBlocks[i].yLocation < 690 && noteBlocks[i].yLocation > 580 && noteBlocks[i].xLocation == 450) {
                noteBlocks.splice(i, 1)
                score++
                document.getElementById("score").innerHTML = score
            }
        }

    }
    //Key S is Pressed : start game 
    if (startGame == false && event.code == "KeyS") {
        noteBlocks = []
        falling = setInterval(blockSpeed, 50 / 3);
        startGame = true
        keyBind1 = "D"
        keyBind2 = "F"
        keyBind3 = "J"
        keyBind4 = "K"
    }


    //Key R is pressed : retry 
    if (misses >= 50 && event.code == "KeyR") {
        score = 0;
        speed = 10;
        misses = 0;
        noteBlocks = [];
        document.getElementById("misses").innerHTML = misses
        document.getElementById("score").innerHTML = score
        document.getElementById('speed').innerHTML = speed
        falling = setInterval(blockSpeed, 50 / 3);
        endGame = false
        keyBind1 = "D"
        keyBind2 = "F"
        keyBind3 = "J"
        keyBind4 = "K"
    }
}


//Make Note Blocks Drop at certain areas
function randomSetValue() {
    let randomVal = Math.randomInt(1, 5)
    if (randomVal == 1) {
        return 0
    }
    else if (randomVal == 2) {
        return 150
    }
    else if (randomVal == 3) {
        return 300
    }
    else if (randomVal == 4) {
        return 450
    }

}

//Display Colour according to xLocation
function randomSetColor(position) {
    if (noteBlocks[position].xLocation == 0) {
        return color[0]
    }
    else if (noteBlocks[position].xLocation == 150) {
        return color[1]

    }
    else if (noteBlocks[position].xLocation == 300) {
        return color[2]
    }
    else if (noteBlocks[position].xLocation == 450) {
        return color[3]
    }
}

//Pushing in blockValues
function noteBlockVals() {
    noteBlocks.push({
        xLocation: randomSetValue(),
        yLocation: -70,
        x: 150,
        y: 70,
    })
}


//Times when to push next block
setTimeout(makeNoteBlocks, 0)
function makeNoteBlocks() {
    noteBlockVals()
    setTimeout(makeNoteBlocks, 3000 / speed);

}

//Make Blocks Falls
let falling = setInterval(blockSpeed, 50 / 3);

function blockSpeed() {
    speed += 0.001

    //Program Speed
    for (let i = 0; i < noteBlocks.length; i++) {
        noteBlocks[i].yLocation += speed
        document.getElementById("speed").innerHTML = Math.round(speed)

        //Remove a noteblock when it reaches the end
        if (noteBlocks[i].yLocation > cnv.height) {
            noteBlocks.splice(i, 1)
            misses++
            document.getElementById("misses").innerHTML = misses
        }
        //Set losing Screen and retry screen
        if (misses >= 50) {
            noteBlocks = []
            clearInterval(falling)
            endGame = true
        }
    }
}






