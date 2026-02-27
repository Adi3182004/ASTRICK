window.addEventListener("load", windowLoadHandler, false);

var sphereRad = 140;
var radius_sp = 1;

var Debugger = function () {};
Debugger.log = function (message) {
  try {
    console.log(message);
  } catch (e) {}
};

function windowLoadHandler() {
  canvasApp();
}

function canvasSupport() {
  return !!document.createElement("canvas").getContext;
}

function canvasApp() {
  if (!canvasSupport()) return;

  var theCanvas = document.getElementById("canvasOne");
  if (!theCanvas) {
    console.warn("canvasOne not found — particle system skipped");
    return;
  }

  var context = theCanvas.getContext("2d");

  var displayWidth;
  var displayHeight;
  var timer;
  var wait;
  var count;
  var numToAddEachFrame;
  var particleList;
  var recycleBin;
  var particleAlpha;
  var r, g, b;
  var fLen;
  var m;
  var projCenterX;
  var projCenterY;
  var zMax;
  var turnAngle;
  var turnSpeed;
  var sphereCenterX, sphereCenterY, sphereCenterZ;
  var particleRad;
  var zeroAlphaDepth;
  var randAccelX, randAccelY, randAccelZ;
  var gravity;
  var rgbString;
  var p;
  var outsideTest;
  var nextParticle;
  var sinAngle;
  var cosAngle;
  var rotX, rotZ;
  var depthAlphaFactor;
  var i;
  var theta, phi;
  var x0, y0, z0;

  init();

  function init() {
    wait = 1;
    count = wait - 1;
    numToAddEachFrame = 8;

    r = 0;
    g = 72;
    b = 255;

    rgbString = "rgba(" + r + "," + g + "," + b + ",";
    particleAlpha = 1;

    displayWidth = theCanvas.width;
    displayHeight = theCanvas.height;

    fLen = 320;
    projCenterX = displayWidth / 2;
    projCenterY = displayHeight / 2;
    zMax = fLen - 2;

    particleList = {};
    recycleBin = {};

    randAccelX = 0.1;
    randAccelY = 0.1;
    randAccelZ = 0.1;

    gravity = 0;
    particleRad = 1.8;

    sphereCenterX = 0;
    sphereCenterY = 0;
    sphereCenterZ = -3 - sphereRad;

    zeroAlphaDepth = -750;

    turnSpeed = (2 * Math.PI) / 1200;
    turnAngle = 0;

    timer = setInterval(onTimer, 40);
  }

  function onTimer() {
    count++;
    if (count >= wait) {
      count = 0;

      for (i = 0; i < numToAddEachFrame; i++) {
        theta = Math.random() * 2 * Math.PI;
        phi = Math.acos(Math.random() * 2 - 1);

        x0 = sphereRad * Math.sin(phi) * Math.cos(theta);
        y0 = sphereRad * Math.sin(phi) * Math.sin(theta);
        z0 = sphereRad * Math.cos(phi);

        var p = addParticle(
          x0,
          sphereCenterY + y0,
          sphereCenterZ + z0,
          0.002 * x0,
          0.002 * y0,
          0.002 * z0,
        );

        p.attack = 50;
        p.hold = 50;
        p.decay = 100;
        p.initValue = 0;
        p.holdValue = particleAlpha;
        p.lastValue = 0;
        p.stuckTime = 90 + Math.random() * 20;
        p.accelX = 0;
        p.accelY = gravity;
        p.accelZ = 0;
      }
    }

    turnAngle = (turnAngle + turnSpeed) % (2 * Math.PI);
    sinAngle = Math.sin(turnAngle);
    cosAngle = Math.cos(turnAngle);

    context.clearRect(0, 0, displayWidth, displayHeight);

    p = particleList.first;
    while (p != null) {
      nextParticle = p.next;
      p.age++;

      if (p.age > p.stuckTime) {
        p.velX += p.accelX + randAccelX * (Math.random() * 2 - 1);
        p.velY += p.accelY + randAccelY * (Math.random() * 2 - 1);
        p.velZ += p.accelZ + randAccelZ * (Math.random() * 2 - 1);

        p.x += p.velX;
        p.y += p.velY;
        p.z += p.velZ;
      }

      rotX = cosAngle * p.x + sinAngle * (p.z - sphereCenterZ);
      rotZ = -sinAngle * p.x + cosAngle * (p.z - sphereCenterZ) + sphereCenterZ;

      m = (radius_sp * fLen) / (fLen - rotZ);
      p.projX = rotX * m + projCenterX;
      p.projY = p.y * m + projCenterY;

      depthAlphaFactor = 1 - rotZ / zeroAlphaDepth;
      depthAlphaFactor = Math.max(0, Math.min(1, depthAlphaFactor));

      context.fillStyle = rgbString + depthAlphaFactor * p.alpha + ")";
      context.beginPath();
      context.arc(p.projX, p.projY, m * particleRad, 0, 2 * Math.PI);
      context.fill();

      p = nextParticle;
    }
  }

  function addParticle(x0, y0, z0, vx0, vy0, vz0) {
    var newParticle = {};
    particleList.first = newParticle;

    newParticle.x = x0;
    newParticle.y = y0;
    newParticle.z = z0;
    newParticle.velX = vx0;
    newParticle.velY = vy0;
    newParticle.velZ = vz0;
    newParticle.age = 0;
    newParticle.dead = false;

    return newParticle;
  }
}

$(function () {
  if ($("#slider-range").length) {
    $("#slider-range").slider({
      range: false,
      min: 20,
      max: 500,
      value: 280,
      slide: function (event, ui) {
        sphereRad = ui.value;
      },
    });
  }

  if ($("#slider-test").length) {
    $("#slider-test").slider({
      range: false,
      min: 1.0,
      max: 2.0,
      value: 1,
      step: 0.01,
      slide: function (event, ui) {
        radius_sp = ui.value;
      },
    });
  }
});
