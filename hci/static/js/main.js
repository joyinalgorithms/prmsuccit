// Main JavaScript file for CCIT website
document.addEventListener("DOMContentLoaded", () => {
  // Initialize all components
  initializeNavigation()
  initializeScrollAnimations()
  initializeBinaryAnimation()
  initializeCounters()
  initializeBackToTop()
  initializeLoadingScreen()
  initializeLazyLoading()

  // SEO and Performance optimizations
  initializeSEOOptimizations()
})

// Navigation functionality
function initializeNavigation() {
  const navbar = document.getElementById("navbar")
  const navToggle = document.getElementById("nav-toggle")
  const navMenu = document.getElementById("nav-menu")
  const navLinks = document.querySelectorAll(".nav-link")

  // Navbar scroll effect
  let lastScrollTop = 0
  window.addEventListener("scroll", () => {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop

    if (scrollTop > 100) {
      navbar.classList.add("scrolled")
    } else {
      navbar.classList.remove("scrolled")
    }

    // Hide navbar on scroll down, show on scroll up
    if (scrollTop > lastScrollTop && scrollTop > 200) {
      navbar.style.transform = "translateY(-100%)"
    } else {
      navbar.style.transform = "translateY(0)"
    }
    lastScrollTop = scrollTop
  })

  // Mobile menu toggle
  if (navToggle && navMenu) {
    navToggle.addEventListener("click", () => {
      navToggle.classList.toggle("active")
      navMenu.classList.toggle("active")
      document.body.classList.toggle("nav-open")
    })
  }

  // Close mobile menu when clicking on links
  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      if (navMenu.classList.contains("active")) {
        navToggle.classList.remove("active")
        navMenu.classList.remove("active")
        document.body.classList.remove("nav-open")
      }
    })
  })

  // Close mobile menu when clicking outside
  document.addEventListener("click", (event) => {
    if (!navbar.contains(event.target) && navMenu.classList.contains("active")) {
      navToggle.classList.remove("active")
      navMenu.classList.remove("active")
      document.body.classList.remove("nav-open")
    }
  })

  // Highlight active navigation link
  highlightActiveNavLink()
}

function highlightActiveNavLink() {
  const currentPath = window.location.pathname
  const navLinks = document.querySelectorAll(".nav-link")

  navLinks.forEach((link) => {
    const linkPath = new URL(link.href).pathname
    if (linkPath === currentPath) {
      link.classList.add("active")
    } else {
      link.classList.remove("active")
    }
  })
}

// Scroll animations using Intersection Observer
function initializeScrollAnimations() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible")

        // Trigger counter animation if it's a counter element
        if (entry.target.classList.contains("animate-counter")) {
          animateCounter(entry.target)
        }
      }
    })
  }, observerOptions)

  // Observe all elements with animation classes
  const animatedElements = document.querySelectorAll(".animate-on-scroll, .animate-counter")
  animatedElements.forEach((element) => {
    observer.observe(element)
  })
}

// Binary animation for hero section
function initializeBinaryAnimation() {
  const binaryContainer = document.getElementById("binaryAnimation")
  if (!binaryContainer) return

  const binaryChars = ["0", "1"]
  const numberOfElements = 50

  function createBinaryElement() {
    const element = document.createElement("div")
    element.className = "binary-digit"
    element.textContent = binaryChars[Math.floor(Math.random() * binaryChars.length)]

    // Random position and animation duration
    element.style.left = Math.random() * 100 + "%"
    element.style.animationDuration = Math.random() * 10 + 5 + "s"
    element.style.animationDelay = Math.random() * 5 + "s"
    element.style.fontSize = Math.random() * 0.8 + 0.8 + "rem"

    binaryContainer.appendChild(element)

    // Remove element after animation completes
    setTimeout(() => {
      if (element.parentNode) {
        element.parentNode.removeChild(element)
      }
    }, 15000)
  }

  // Create initial elements
  for (let i = 0; i < numberOfElements; i++) {
    setTimeout(() => createBinaryElement(), i * 200)
  }

  // Continuously create new elements
  setInterval(createBinaryElement, 1000)
}

// Counter animation
function animateCounter(element) {
  const target = Number.parseInt(element.getAttribute("data-target"))
  const duration = 2000 // 2 seconds
  const increment = target / (duration / 16) // 60fps
  let current = 0

  const timer = setInterval(() => {
    current += increment
    if (current >= target) {
      current = target
      clearInterval(timer)
    }
    element.textContent = Math.floor(current)
  }, 16)
}

// Initialize all counters
function initializeCounters() {
  const counters = document.querySelectorAll(".stat-number[data-target]")
  counters.forEach((counter) => {
    counter.textContent = "0"
  })
}

// Back to top button
function initializeBackToTop() {
  const backToTopButton = document.getElementById("backToTop")
  if (!backToTopButton) return

  window.addEventListener("scroll", () => {
    if (window.pageYOffset > 300) {
      backToTopButton.classList.add("visible")
    } else {
      backToTopButton.classList.remove("visible")
    }
  })

  backToTopButton.addEventListener("click", () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    })
  })
}

// Loading screen
function initializeLoadingScreen() {
  const loadingScreen = document.getElementById("loadingScreen")
  if (!loadingScreen) return

  window.addEventListener("load", () => {
    setTimeout(() => {
      loadingScreen.classList.add("hidden")
      setTimeout(() => {
        loadingScreen.style.display = "none"
      }, 500)
    }, 1000)
  })
}

// Lazy loading for images
function initializeLazyLoading() {
  if ("IntersectionObserver" in window) {
    const imageObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const img = entry.target
          img.src = img.dataset.src || img.src
          img.classList.remove("lazy")
          imageObserver.unobserve(img)
        }
      })
    })

    const lazyImages = document.querySelectorAll('img[loading="lazy"]')
    lazyImages.forEach((img) => {
      imageObserver.observe(img)
    })
  }
}

// SEO and Performance optimizations
function initializeSEOOptimizations() {
  // Add structured data for better SEO
  addStructuredData()

  // Preload critical resources
  preloadCriticalResources()

  // Initialize service worker for caching (if available)
  initializeServiceWorker()
}

function addStructuredData() {
  const structuredData = {
    "@context": "https://schema.org",
    "@type": "EducationalOrganization",
    name: "College of Communication and Information Technology",
    alternateName: "CCIT",
    url: window.location.origin,
    description: "Leading education in Computer Science and Information Technology",
    address: {
      "@type": "PostalAddress",
      addressLocality: "University Campus",
      addressRegion: "State",
      addressCountry: "Country",
    },
    contactPoint: {
      "@type": "ContactPoint",
      telephone: "+1-555-123-4567",
      contactType: "customer service",
      email: "info@ccit.edu",
    },
    sameAs: ["https://facebook.com/ccit", "https://twitter.com/ccit", "https://linkedin.com/school/ccit"],
  }

  const script = document.createElement("script")
  script.type = "application/ld+json"
  script.textContent = JSON.stringify(structuredData)
  document.head.appendChild(script)
}

function preloadCriticalResources() {
  // Preload hero background image
  const heroImage = new Image()
  heroImage.src = "/static/images/ccit-building.jpg"

  // Preload critical fonts
  const fontLink = document.createElement("link")
  fontLink.rel = "preload"
  fontLink.href = "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap"
  fontLink.as = "style"
  document.head.appendChild(fontLink)
}

function initializeServiceWorker() {
  if ("serviceWorker" in navigator) {
    window.addEventListener("load", () => {
      navigator.serviceWorker
        .register("/static/js/sw.js")
        .then((registration) => {
          console.log("ServiceWorker registration successful")
        })
        .catch((err) => {
          console.log("ServiceWorker registration failed")
        })
    })
  }
}

// Utility functions
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

function throttle(func, limit) {
  let inThrottle
  return function () {
    const args = arguments

    if (!inThrottle) {
      func.apply(this, args)
      inThrottle = true
      setTimeout(() => (inThrottle = false), limit)
    }
  }
}

// Error handling
window.addEventListener("error", (event) => {
  console.error("JavaScript error:", event.error)
  // You could send this to an error tracking service
})

// Performance monitoring
if ("performance" in window) {
  window.addEventListener("load", () => {
    setTimeout(() => {
      const perfData = performance.getEntriesByType("navigation")[0]
      console.log("Page load time:", perfData.loadEventEnd - perfData.loadEventStart, "ms")
    }, 0)
  })
}

// Accessibility improvements
function initializeAccessibility() {
  // Skip to main content link
  const skipLink = document.createElement("a")
  skipLink.href = "#main-content"
  skipLink.textContent = "Skip to main content"
  skipLink.className = "skip-link"
  skipLink.style.cssText = `
        position: absolute;
        top: -40px;
        left: 6px;
        background: #000;
        color: #fff;
        padding: 8px;
        text-decoration: none;
        z-index: 10000;
        transition: top 0.3s;
    `

  skipLink.addEventListener("focus", function () {
    this.style.top = "6px"
  })

  skipLink.addEventListener("blur", function () {
    this.style.top = "-40px"
  })

  document.body.insertBefore(skipLink, document.body.firstChild)

  // Keyboard navigation for dropdowns
  const dropdownToggles = document.querySelectorAll(".dropdown-toggle")
  dropdownToggles.forEach((toggle) => {
    toggle.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault()
        this.click()
      }
    })
  })
}

// Initialize accessibility features
initializeAccessibility()

// Form validation (if forms exist)
function initializeFormValidation() {
  const forms = document.querySelectorAll("form")
  forms.forEach((form) => {
    form.addEventListener("submit", function (e) {
      if (!validateForm(this)) {
        e.preventDefault()
      }
    })
  })
}

function validateForm(form) {
  let isValid = true
  const requiredFields = form.querySelectorAll("[required]")

  requiredFields.forEach((field) => {
    if (!field.value.trim()) {
      showFieldError(field, "This field is required")
      isValid = false
    } else {
      clearFieldError(field)
    }
  })

  return isValid
}

function showFieldError(field, message) {
  clearFieldError(field)
  const errorElement = document.createElement("div")
  errorElement.className = "field-error"
  errorElement.textContent = message
  errorElement.style.color = "#e74c3c"
  errorElement.style.fontSize = "0.875rem"
  errorElement.style.marginTop = "0.25rem"

  field.parentNode.appendChild(errorElement)
  field.style.borderColor = "#e74c3c"
}

function clearFieldError(field) {
  const existingError = field.parentNode.querySelector(".field-error")
  if (existingError) {
    existingError.remove()
  }
  field.style.borderColor = ""
}

// Initialize form validation
initializeFormValidation()

// Console welcome message
console.log(
  `
%c🎓 Welcome to CCIT Website!
%cCollege of Communication and Information Technology
%cBuilt with modern web technologies and best practices.
`,
  "color: #3498db; font-size: 18px; font-weight: bold;",
  "color: #2c3e50; font-size: 14px;",
  "color: #95a5a6; font-size: 12px;",
)
