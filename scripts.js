/* scripts.js
   Global JavaScript for 4NOX WAV
*/

document.addEventListener('DOMContentLoaded', () => {
    // 1. Dynamic Year in Footer
    const yearSpan = document.getElementById('year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    // 2. Mobile Menu Toggle
    const mobileBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileLinks = document.querySelectorAll('.mobile-link');
    
    if (mobileBtn && mobileMenu) {
        mobileBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
        
        // Close mobile menu when a link is clicked
        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
            });
        });
    }

    // 3. Subtle Navbar Background Change on Scroll
    const nav = document.querySelector('nav');
    if (nav) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                nav.classList.add('shadow-lg', 'shadow-black/50');
            } else {
                nav.classList.remove('shadow-lg', 'shadow-black/50');
            }
        });
    }

    // 4. Privacy Notice Logic (from legacy site)
    const privacyNotice = document.getElementById('privacyNotice');
    const acceptButton = document.getElementById('acceptButton');

    if (privacyNotice && acceptButton) {
        // Check if user already accepted
        if (!localStorage.getItem('privacyAccepted')) {
            privacyNotice.style.display = 'flex';
        } else {
            privacyNotice.style.display = 'none';
        }

        acceptButton.addEventListener('click', () => {
            localStorage.setItem('privacyAccepted', 'true');
            privacyNotice.style.display = 'none';
        });
    }
});

// Global copy to clipboard function
window.copyEmail = function(email, element, isText = false) {
    navigator.clipboard.writeText(email).then(() => {
        const originalHtml = element.innerHTML;
        if (isText) {
            element.innerHTML = 'Skopiowano!';
        } else {
            element.innerHTML = '<span class="font-bold text-xs">✓</span>';
        }
        
        setTimeout(() => {
            element.innerHTML = originalHtml;
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy text: ', err);
    });
};

// --- EmailJS Contact Form Logic ---
document.addEventListener("DOMContentLoaded", () => {
    const contactForm = document.getElementById("contact-form");
    const statusMessage = document.getElementById("status-message");

    if (contactForm && typeof emailjs !== 'undefined') {
        // Initialize EmailJS with user's Public Key
        emailjs.init("KhhpDMoVBpGtqgSjM");

        contactForm.addEventListener("submit", async (event) => {
            event.preventDefault();
            const form = event.target;
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn.textContent;
            
            submitBtn.textContent = 'Sending...';
            submitBtn.disabled = true;
            if (statusMessage) {
                statusMessage.textContent = "Sending your message...";
                statusMessage.className = "mt-4 text-center text-sm text-zinc-400";
            }

            try {
                const response = await emailjs.sendForm(
                    "service_kf463es",
                    "template_q83n3iv",
                    form
                );
                console.log("Email sent successfully!", response);
                form.reset();
                if (statusMessage) {
                    statusMessage.textContent = "Message sent successfully! We will get back to you soon.";
                    statusMessage.classList.add("text-green-500");
                    statusMessage.classList.remove("text-zinc-400");
                }
            } catch (error) {
                console.error("Failed to send email:", error);
                if (statusMessage) {
                    statusMessage.textContent = "Oops! Something went wrong. Please try again or use our direct email.";
                    statusMessage.classList.add("text-red-500");
                    statusMessage.classList.remove("text-zinc-400");
                }
            } finally {
                submitBtn.textContent = originalBtnText;
                submitBtn.disabled = false;
            }
        });
    }
});
