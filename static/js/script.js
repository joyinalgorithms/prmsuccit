// Mobile Navigation Toggle
document.addEventListener("DOMContentLoaded", () => {
  // Initialize slideshow
  initializeSlideshow()

  const navToggle = document.getElementById("nav-toggle")
  const navMenu = document.getElementById("nav-menu")

  if (navToggle && navMenu) {
    navToggle.addEventListener("click", () => {
      navMenu.classList.toggle("active")
      navToggle.classList.toggle("active")
    })

    // Close menu when clicking on a link
    const navLinks = document.querySelectorAll(".nav-link")
    navLinks.forEach((link) => {
      link.addEventListener("click", () => {
        navMenu.classList.remove("active")
        navToggle.classList.remove("active")
      })
    })

    // Close menu when clicking outside
    document.addEventListener("click", (event) => {
      if (!navToggle.contains(event.target) && !navMenu.contains(event.target)) {
        navMenu.classList.remove("active")
        navToggle.classList.remove("active")
      }
    })
  }
})

// Enhanced Binary Animation
function createBinaryParticles() {
  const binaryBackground = document.querySelector(".binary-background")
  if (!binaryBackground) return

  // Create floating binary particles
  for (let i = 0; i < 20; i++) {
    const particle = document.createElement("div")
    particle.className = "binary-particle"
    particle.textContent = Math.random() > 0.5 ? "1" : "0"
    particle.style.cssText = `
            position: absolute;
            font-family: 'JetBrains Mono', monospace;
            font-size: ${Math.random() * 20 + 10}px;
            color: rgba(102, 126, 234, ${Math.random() * 0.3 + 0.1});
            left: ${Math.random() * 100}%;
            top: ${Math.random() * 100}%;
            pointer-events: none;
            animation: floatBinary ${Math.random() * 20 + 10}s linear infinite;
            animation-delay: ${Math.random() * 5}s;
        `
    binaryBackground.appendChild(particle)
  }
}

// CSS for binary particle animation
const style = document.createElement("style")
style.textContent = `
    @keyframes floatBinary {
        0% {
            transform: translateY(100vh) rotate(0deg);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        100% {
            transform: translateY(-100vh) rotate(360deg);
            opacity: 0;
        }
    }
`
document.head.appendChild(style)

// Initialize binary particles
createBinaryParticles()

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault()
    const target = document.querySelector(this.getAttribute("href"))
    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
        block: "start",
      })
    }
  })
})

// Header scroll effect
window.addEventListener("scroll", () => {
  const header = document.querySelector(".header")
  if (header) {
    if (window.scrollY > 100) {
      header.style.background = "rgba(10, 10, 10, 0.98)"
      header.style.boxShadow = "0 2px 20px rgba(0, 0, 0, 0.3)"
    } else {
      header.style.background = "rgba(10, 10, 10, 0.95)"
      header.style.boxShadow = "none"
    }
  }
})

// Intersection Observer for animations
const observerOptions = {
  threshold: 0.1,
  rootMargin: "0px 0px -50px 0px",
}

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("fade-in-up")
    }
  })
}, observerOptions)

// Observe elements for animation
document.addEventListener("DOMContentLoaded", () => {
  const animateElements = document.querySelectorAll(
    ".feature-card, .program-card, .faculty-card, .news-card, .organization-card, .department-card",
  )
  animateElements.forEach((el) => observer.observe(el))
})

// Newsletter form handling
const newsletterForm = document.querySelector(".newsletter-form")
if (newsletterForm) {
  newsletterForm.addEventListener("submit", function (e) {
    e.preventDefault()
    const email = this.querySelector(".newsletter-input").value

    if (email) {
      // Simulate form submission
      const button = this.querySelector(".btn")
      const originalText = button.textContent
      button.textContent = "Subscribing..."
      button.disabled = true

      setTimeout(() => {
        button.textContent = "Subscribed!"
        button.style.background = "#50fa7b"

        setTimeout(() => {
          button.textContent = originalText
          button.disabled = false
          button.style.background = ""
          this.reset()
        }, 2000)
      }, 1000)
    }
  })
}

// Dynamic typing effect for hero section
function typeWriter(element, text, speed = 100) {
  if (!element) return

  let i = 0
  element.textContent = ""

  function type() {
    if (i < text.length) {
      element.textContent += text.charAt(i)
      i++
      setTimeout(type, speed)
    }
  }

  type()
}

// Initialize typing effect on hero page
document.addEventListener("DOMContentLoaded", () => {
  const heroTitle = document.querySelector(".hero-title")
  if (heroTitle && window.location.pathname === "/") {
    const originalText = heroTitle.textContent
    setTimeout(() => {
      typeWriter(heroTitle, originalText, 50)
    }, 500)
  }
})

// Code block syntax highlighting effect
document.addEventListener("DOMContentLoaded", () => {
  const codeBlocks = document.querySelectorAll(".code-block")
  codeBlocks.forEach((block) => {
    const lines = block.querySelectorAll(".code-line")
    lines.forEach((line, index) => {
      line.style.opacity = "0"
      line.style.transform = "translateX(-20px)"

      setTimeout(
        () => {
          line.style.transition = "all 0.5s ease"
          line.style.opacity = "1"
          line.style.transform = "translateX(0)"
        },
        index * 200 + 1000,
      )
    })
  })
})

// Stats counter animation
function animateCounter(element, target, duration = 2000) {
  const start = 0
  const increment = target / (duration / 16)
  let current = start

  const timer = setInterval(() => {
    current += increment
    if (current >= target) {
      current = target
      clearInterval(timer)
    }

    if (target >= 1000) {
      element.textContent = Math.floor(current).toLocaleString() + "+"
    } else if (target.toString().includes("%")) {
      element.textContent = Math.floor(current) + "%"
    } else {
      element.textContent = Math.floor(current) + "+"
    }
  }, 16)
}

// Initialize counter animations
const statsObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const statNumber = entry.target.querySelector(".stat-number")
        if (statNumber && !statNumber.classList.contains("animated")) {
          statNumber.classList.add("animated")
          const text = statNumber.textContent
          const number = Number.parseInt(text.replace(/[^\d]/g, ""))
          animateCounter(statNumber, number)
        }
      }
    })
  },
  { threshold: 0.5 },
)

document.addEventListener("DOMContentLoaded", () => {
  const statItems = document.querySelectorAll(".stat-item")
  statItems.forEach((item) => statsObserver.observe(item))
})

// Enhanced error page interactions
document.addEventListener("DOMContentLoaded", () => {
  const errorCode = document.querySelector(".error-number")
  if (errorCode) {
    // Add glitch effect on hover
    errorCode.addEventListener("mouseenter", function () {
      this.style.animation = "glitch 0.5s ease-in-out"
    })

    errorCode.addEventListener("animationend", function () {
      this.style.animation = ""
    })
  }
})

// Add glitch animation CSS
const glitchStyle = document.createElement("style")
glitchStyle.textContent = `
    @keyframes glitch {
        0% { transform: translate(0); }
        20% { transform: translate(-2px, 2px); }
        40% { transform: translate(-2px, -2px); }
        60% { transform: translate(2px, 2px); }
        80% { transform: translate(2px, -2px); }
        100% { transform: translate(0); }
    }
`
document.head.appendChild(glitchStyle)

// Lazy loading for images
document.addEventListener("DOMContentLoaded", () => {
  const images = document.querySelectorAll("img[src]")

  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const img = entry.target
        img.style.opacity = "1"
        img.style.transition = "opacity 0.5s ease"

        img.onload = function () {
          this.style.opacity = "1"
        }

        observer.unobserve(img)
      }
    })
  })

  images.forEach((img) => imageObserver.observe(img))
})

// Keyboard navigation enhancement
document.addEventListener("keydown", (e) => {
  // ESC key closes mobile menu
  if (e.key === "Escape") {
    const navMenu = document.getElementById("nav-menu")
    const navToggle = document.getElementById("nav-toggle")
    if (navMenu && navToggle) {
      navMenu.classList.remove("active")
      navToggle.classList.remove("active")
    }
  }
})

// Performance optimization: Debounce scroll events
function debounce(func, wait) {
  let timeout
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout)
      func(...args)
    }
    clearTimeout(timeout)
    timeout = setTimeout(later, wait)
  }
}

// Apply debounce to scroll handler
const debouncedScrollHandler = debounce(() => {
  const header = document.querySelector(".header")
  if (header) {
    if (window.scrollY > 100) {
      header.style.background = "rgba(10, 10, 10, 0.98)"
      header.style.boxShadow = "0 2px 20px rgba(0, 0, 0, 0.3)"
    } else {
      header.style.background = "rgba(10, 10, 10, 0.95)"
      header.style.boxShadow = "none"
    }
  }
}, 10)

window.addEventListener("scroll", debouncedScrollHandler)

// Console welcome message
console.log(
  `
%c🎓 Welcome to CCIT! 
%cCollege of Computer and Information Technology
%cBuilding the future of technology education

%c💻 Interested in our programs? Visit our website!
%c🚀 Ready to innovate? Join us today!
`,
  "color: #667eea; font-size: 20px; font-weight: bold;",
  "color: #764ba2; font-size: 16px;",
  "color: #50fa7b; font-size: 14px;",
  "color: #8be9fd; font-size: 14px;",
  "color: #ff79c6; font-size: 14px;",
)

// Slideshow functionality
let slideIndex = 0
let slideInterval

function initializeSlideshow() {
  const slides = document.querySelectorAll(".slide")
  const indicators = document.querySelectorAll(".indicator")

  if (slides.length === 0) return

  // Show first slide
  showSlide(0)

  // Start auto-advance
  startSlideshow()
}

function showSlide(index) {
  const slides = document.querySelectorAll(".slide")
  const indicators = document.querySelectorAll(".indicator")

  if (slides.length === 0) return

  // Remove active class from all slides and indicators
  slides.forEach((slide) => slide.classList.remove("active"))
  indicators.forEach((indicator) => indicator.classList.remove("active"))

  // Add active class to current slide and indicator
  if (slides[index]) {
    slides[index].classList.add("active")
  }
  if (indicators[index]) {
    indicators[index].classList.add("active")
  }
}

function changeSlide(direction) {
  const slides = document.querySelectorAll(".slide")
  if (slides.length === 0) return

  slideIndex += direction
  if (slideIndex >= slides.length) slideIndex = 0
  if (slideIndex < 0) slideIndex = slides.length - 1
  showSlide(slideIndex)

  // Restart auto-advance
  restartSlideshow()
}

function currentSlide(index) {
  slideIndex = index
  showSlide(slideIndex)

  // Restart auto-advance
  restartSlideshow()
}

function startSlideshow() {
  slideInterval = setInterval(() => {
    const slides = document.querySelectorAll(".slide")
    if (slides.length > 1) {
      slideIndex = (slideIndex + 1) % slides.length
      showSlide(slideIndex)
    }
  }, 5000)
}

function restartSlideshow() {
  clearInterval(slideInterval)
  startSlideshow()
}
