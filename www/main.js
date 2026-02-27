let isStopped = false;
let isSpeaking = false;
window.addEventListener("load", () => {
  if (window.eel) {
    eel.init()();
  }
});
// Hide stop button and SiriWave on load
$(function () {
  $("#stopBtn").attr("hidden", true);
  $("#SiriWave").attr("hidden", true);
});

$(document).ready(function () {
  eel.expose(showChatAfterSpeech);
  function showChatAfterSpeech() {
    isSpeaking = false;
    isStopped = false;
    $("#SiriWave").attr("hidden", true);
    $("#Oval").attr("hidden", false);
    $("#stopBtn").attr("hidden", true);
  }

  eel.expose(startListening);
  function startListening() {
    startSpeaking();
    eel.allCommands();
  }

  eel.expose(playAssistantSound);
  function playAssistantSound() {
    var audio = new Audio("assets/audio/start_sound.mp3");
    audio.play().catch(function (e) {
      console.warn("Autoplay blocked:", e);
    });
  }

  $(".text").textillate({
    loop: false,
    in: {
      effect: "bounceIn",
      callback: function () {
        $(".text").textillate("stop");
      },
    },
  });

  $(".siri-message").textillate({
    loop: false,
    in: {
      effect: "None",
      callback: function () {
        $(".siri-message").textillate("stop");
      },
    },
  });

  $("#MicBtn").click(function () {
    startSpeaking();
    eel.allCommands();
  });

  function doc_keyUp(e) {
    if (e.key === "j" && e.metaKey) {
      startSpeaking();
      eel.allCommands();
    }
  }
  document.addEventListener("keyup", doc_keyUp, false);

  function startSpeaking() {
    isStopped = false;
    $("#Oval").attr("hidden", true);
    $("#SiriWave").attr("hidden", false);
    $("#stopBtn").removeAttr("hidden");
  }

  function stopSpeaking() {
    isStopped = true;
    isSpeaking = false;

    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
    }

    eel.forceStopTTS();

    $("#SiriWave").attr("hidden", true);
    $("#Oval").attr("hidden", false);
    $("#stopBtn").attr("hidden", true);
  }

  eel.expose(startSpeaking);
  eel.expose(stopSpeaking);

  $("#stopBtn").click(function () {
    stopSpeaking();
  });

  function PlayAssistant(message) {
    if (message !== "" && !isStopped) {
      startSpeaking();
      eel.allCommands(message);
      $("#chatbox").val("");
      $("#MicBtn").attr("hidden", false);
      $("#SendBtn").attr("hidden", true);
    }
  }

  function ShowHideButton(message) {
    if (message.length === 0) {
      $("#MicBtn").attr("hidden", false);
      $("#SendBtn").attr("hidden", true);
    } else {
      $("#MicBtn").attr("hidden", true);
      $("#SendBtn").attr("hidden", false);
    }
  }

  $("#chatbox").keyup(function () {
    let message = $("#chatbox").val();
    ShowHideButton(message);
  });

  $("#SendBtn").click(function () {
    isStopped = false;
    let message = $("#chatbox").val();
    PlayAssistant(message);
  });

  $("#chatbox").keypress(function (e) {
    if (e.which === 13) {
      isStopped = false;
      let message = $("#chatbox").val();
      PlayAssistant(message);
    }
  });
});

/* ===============================
   THREE ORBIT
=============================== */

document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("three-orbit");
  if (!container) return;

  const scene = new THREE.Scene();

  const camera = new THREE.PerspectiveCamera(
    45,
    container.clientWidth / container.clientHeight,
    0.1,
    1000,
  );
  camera.position.z = 5;

  const renderer = new THREE.WebGLRenderer({
    alpha: true,
    antialias: true,
  });
  const width = container.offsetWidth || 440;
  const height = container.offsetHeight || 440;

  renderer.setSize(width, height);
  renderer.setPixelRatio(window.devicePixelRatio);
  container.appendChild(renderer.domElement);

  const textureLoader = new THREE.TextureLoader();
  const ringTexture = textureLoader.load(
    "https://threejs.org/examples/textures/sprites/disc.png",
  );

  function createRing(inner, outer, color, opacity) {
    const geo = new THREE.RingGeometry(inner, outer, 256);

    const mat = new THREE.MeshBasicMaterial({
      map: ringTexture,
      color: color,
      transparent: true,
      side: THREE.DoubleSide,
      opacity: opacity,
      depthWrite: false,
      blending: THREE.AdditiveBlending,
    });

    const mesh = new THREE.Mesh(geo, mat);

    mesh.rotation.x = THREE.MathUtils.degToRad(72);
    mesh.rotation.y = THREE.MathUtils.degToRad(-28);

    scene.add(mesh);
    return mesh;
  }

  const ring1 = createRing(1.35, 1.75, 0x00d4ff, 0.9);
  const ring2 = createRing(1.8, 2.1, 0x8b5cf6, 0.6);
  const ring3 = createRing(2.15, 2.35, 0x00ffff, 0.35);

  const starGeo = new THREE.BufferGeometry();
  const starCount = 120;

  const positions = new Float32Array(starCount * 3);

  for (let i = 0; i < starCount; i++) {
    const radius = 2 + Math.random() * 0.4;
    const angle = Math.random() * Math.PI * 2;

    positions[i * 3] = Math.cos(angle) * radius;
    positions[i * 3 + 1] = Math.sin(angle) * radius;
    positions[i * 3 + 2] = (Math.random() - 0.5) * 0.3;
  }

  starGeo.setAttribute("position", new THREE.BufferAttribute(positions, 3));

  const starMat = new THREE.PointsMaterial({
    color: 0x00d4ff,
    size: 0.025,
    transparent: true,
    opacity: 0.8,
    blending: THREE.AdditiveBlending,
  });

  const stars = new THREE.Points(starGeo, starMat);
  stars.rotation.x = THREE.MathUtils.degToRad(72);
  stars.rotation.y = THREE.MathUtils.degToRad(-28);
  scene.add(stars);

  function animate() {
    requestAnimationFrame(animate);

    ring1.rotation.z += 0.012;
    ring2.rotation.z -= 0.008;
    ring3.rotation.z += 0.004;

    stars.rotation.z += 0.002;

    renderer.render(scene, camera);
  }

  animate();

  window.addEventListener("resize", () => {
    const w = container.clientWidth;
    const h = container.clientHeight;
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
  });
});

/* ===============================
   🔥 RIBBON MOUSE REACT (FIXED)
=============================== */

document.addEventListener("DOMContentLoaded", () => {
  const ribbon = document.querySelector(".astrick-ribbon");
  if (!ribbon) return;

  let targetX = 0;
  let targetY = 0;
  let currentX = 0;
  let currentY = 0;

  document.addEventListener("mousemove", (e) => {
    targetX = (e.clientX / window.innerWidth - 0.5) * 18;
    targetY = (e.clientY / window.innerHeight - 0.5) * 18;
  });

  function smoothMove() {
    currentX += (targetX - currentX) * 0.08;
    currentY += (targetY - currentY) * 0.08;

    ribbon.style.transform = `translate3d(${currentX}px, ${currentY}px, 0)`;
    requestAnimationFrame(smoothMove);
  }

  smoothMove();
});
eel.expose(addAssistantMessage);
function addAssistantMessage(message) {
  if (!message) return;

  const chatBox = document.getElementById("chat-canvas-body");
  if (!chatBox) return;

  chatBox.innerHTML += `
    <div class="receiver_message">
      ${message}
    </div>
  `;

  chatBox.scrollTop = chatBox.scrollHeight;

  const panel = document.getElementById("offcanvasScrolling");
  if (panel && !panel.classList.contains("show")) {
    const bsOffcanvas = bootstrap.Offcanvas.getOrCreateInstance(panel);
    bsOffcanvas.show();
  }
}
