// script.js
// Handles the interactive gift box and simple confetti effect

document.addEventListener('DOMContentLoaded', () => {
  const giftBox = document.getElementById('giftBox');
  const surpriseCard = document.getElementById('surpriseCard');
  const canvas = document.getElementById('confettiCanvas');

  // ---------- Gift Box Interaction ----------
  if (giftBox && surpriseCard) {
    giftBox.addEventListener('click', () => {
      // Open the box
      giftBox.classList.add('opened');
      // Reveal the surprise card after short delay
      setTimeout(() => {
        surpriseCard.classList.add('show');
        launchConfetti();
      }, 600);
    });
  }

  // ---------- Simple Confetti ----------
  const confettiColors = ["#fce18a", "#ff726d", "#b48def", "#f4306d"];
  const confettiCount = 150;
  let particles = [];
  let ctx;

  function initConfetti() {
    ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    particles = [];
    for (let i = 0; i < confettiCount; i++) {
      particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * -canvas.height,
        r: Math.random() * 6 + 4,
        d: Math.random() * confettiCount + 10,
        color: confettiColors[Math.floor(Math.random() * confettiColors.length)],
        tilt: Math.random() * 10 - 10,
        tiltAngleIncremental: (Math.random() * 0.07) + 0.05,
        tiltAngle: 0
      });
    }
  }

  function drawConfetti() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => {
      ctx.beginPath();
      ctx.lineWidth = p.r;
      ctx.strokeStyle = p.color;
      ctx.moveTo(p.x + p.tilt + p.r / 2, p.y);
      ctx.lineTo(p.x + p.tilt, p.y + p.tilt + p.r / 2);
      ctx.stroke();
    });
    updateConfetti();
  }

  function updateConfetti() {
    particles.forEach(p => {
      p.tiltAngle += p.tiltAngleIncremental;
      p.y += (Math.cos(p.d) + 3 + p.r / 2) / 2;
      p.x += Math.sin(0);
      p.tilt = Math.sin(p.tiltAngle - (p.d / 3)) * 15;
      // Reset when out of view
      if (p.y > canvas.height) {
        p.x = Math.random() * canvas.width;
        p.y = -20;
        p.tilt = Math.random() * 10 - 10;
      }
    });
  }

  let confettiAnimationId;

  function launchConfetti() {
    initConfetti();
    const render = () => {
      drawConfetti();
      confettiAnimationId = requestAnimationFrame(render);
    };
    render();
    // Stop after 5 seconds
    setTimeout(() => {
      cancelAnimationFrame(confettiAnimationId);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    }, 5000);
  }
});
