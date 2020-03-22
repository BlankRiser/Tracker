/*
  Johan Karlsson, 2020
  https://twitter.com/DonKarlssonSan
  MIT License, see Details View
*/
let canvas;
let ctx;
let w, h;
let colors;

function setup() {
    canvas = document.querySelector("#canvas");
    ctx = canvas.getContext("2d");
    reset();
    window.addEventListener("resize", () => {
        reset();
        draw();
    });
    canvas.addEventListener("click", draw);
    setupColors();
}

function reset() {
    w = canvas.width = window.innerWidth;
    // h = canvas.height = window.innerHeight;
    h = canvas.height =500;
}

function draw() {
    let colorTheme = getRandomColorTheme();
    ctx.fillRect(0, 0, w, h);
    let size = 300;
    let diag = Math.sqrt(size * size * 2);
    let nrOfColumns = Math.round(w / diag * 2) + 1;
    let nrOfRows = Math.round(h / diag * 4) + 2;
    for (let row = 0; row < nrOfRows; row++) {
        let y = row * diag / 4;
        for (let col = 0; col < nrOfColumns; col++) {
            let x = col * diag / 2;
            let xOffset = row % 2 * diag / 4;
            drawRects(x + xOffset, y, size, colorTheme);
        }
    }
}

function setupColors() {
    colors = [
        //https://coolors.co/app/000000-ffffff-494949-7c7a7a-ff5d73
        [
            "#000000",
            "#ffffff",
            "#494949",
            "#7c7a7a",
            "#ff5d73"
        ],
        //https://coolors.co/app/6699cc-fff275-ff8c42-ff3c38-a23e48
        [
            "#6699cc",
            "#fff275",
            "#ff8c42",
            "#ff3c38",
            "#a23e48"
        ],
        //https://coolors.co/app/231942-5e548e-9f86c0-be95c4-e0b1cb
        [
            "#231942",
            "#5e548e",
            "#9f86c0",
            "#be95c4",
            "#e0b1cb"
        ],
        //https://coolors.co/ffffff-81f4e1-56cbf9-ff729f-d3c4d1
        [
            "#ffffff",
            "#81f4e1",
            "#56cbf9",
            "#ff729f",
            "#d3c4d1"
        ],
    ];
}

function getRandomColorTheme() {
    let index = Math.floor(Math.random() * colors.length);
    return colors[index];
}

function drawRects(x, y, size, colorTheme) {
    ctx.save();
    ctx.translate(x, y);
    ctx.rotate(Math.PI / 4);
    let nrOfRects = 6;
    let colorOffset = Math.floor(Math.random() * colorTheme.length);
    for (let i = 0; i < nrOfRects; i++) {
        ctx.fillStyle = colorTheme[(i + colorOffset) % colorTheme.length];
        let currentSize = (nrOfRects - i) * size / nrOfRects;
        if (i === 0) {
            ctx.shadowColor = "black";
            ctx.shadowBlur = 30;
        } else {
            ctx.shadowColor = undefined;
            ctx.shadowBlur = 0;
        }
        ctx.fillRect(-currentSize / 2, -currentSize / 2, currentSize, currentSize);
    }
    ctx.restore();
}


setup();
draw();