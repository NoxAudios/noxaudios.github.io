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

    // 4. Privacy Notice Logic
    const privacyNotice = document.getElementById('privacyNotice');
    const acceptButton = document.getElementById('acceptButton');

    if (privacyNotice && acceptButton) {
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

    // 5. FAQ Accordion Logic
    const faqButtons = document.querySelectorAll('.faq-btn');
    faqButtons.forEach(button => {
        button.addEventListener('click', () => {
            const content = button.nextElementSibling;
            const icon = button.querySelector('.faq-icon');
            const isOpen = content.style.maxHeight && content.style.maxHeight !== '0px';
            
            // Close all other FAQs in the same container
            const parent = button.closest('.faq-container') || document;
            parent.querySelectorAll('.faq-content').forEach(item => {
                item.style.maxHeight = null;
            });
            parent.querySelectorAll('.faq-icon').forEach(item => {
                item.classList.remove('rotate-180');
            });
            
            // Toggle clicked FAQ
            if (!isOpen) {
                content.style.maxHeight = content.scrollHeight + "px";
                if (icon) icon.classList.add('rotate-180');
            }
        });
    });

    // 6. Pricing & Pre-selection CTA logic
    const selectServiceTriggers = document.querySelectorAll('[data-service-select]');
    const serviceSelect = document.getElementById('service-select');
    
    selectServiceTriggers.forEach(trigger => {
        trigger.addEventListener('click', (e) => {
            const targetService = trigger.getAttribute('data-service-select');
            if (serviceSelect && targetService) {
                serviceSelect.value = targetService;
                // Dispatch change event in case any listener needs it
                serviceSelect.dispatchEvent(new Event('change'));
            }
        });
    });

    // 7. Pricing / Scope Carousel Logic
    const track = document.getElementById('pricing-slider-track');
    const container = document.getElementById('pricing-carousel-container');
    const prevBtn = document.getElementById('pricing-prev-btn');
    const nextBtn = document.getElementById('pricing-next-btn');
    const stepDisplay = document.getElementById('pricing-current-step');
    const dots = document.querySelectorAll('.pricing-dot');
    
    if (track && container) {
        let currentIndex = 0;
        const totalScreens = 3;

        function updateSlider(index) {
            if (index < 0) index = 0;
            if (index >= totalScreens) index = totalScreens - 1;
            currentIndex = index;

            // Move track
            track.style.transform = `translateX(-${currentIndex * 100}%)`;

            // Update number indicator
            if (stepDisplay) {
                stepDisplay.textContent = `0${currentIndex + 1}`;
            }

            // Update dots
            dots.forEach((dot, idx) => {
                if (idx === currentIndex) {
                    dot.classList.remove('w-4', 'bg-zinc-800');
                    dot.classList.add('w-8', 'bg-white');
                    dot.setAttribute('aria-selected', 'true');
                } else {
                    dot.classList.remove('w-8', 'bg-white');
                    dot.classList.add('w-4', 'bg-zinc-800');
                    dot.setAttribute('aria-selected', 'false');
                }
            });

            // Update buttons disabled state styling
            if (prevBtn) {
                if (currentIndex === 0) {
                    prevBtn.classList.add('opacity-40', 'cursor-not-allowed');
                } else {
                    prevBtn.classList.remove('opacity-40', 'cursor-not-allowed');
                }
            }
            if (nextBtn) {
                if (currentIndex === totalScreens - 1) {
                    nextBtn.classList.add('opacity-40', 'cursor-not-allowed');
                } else {
                    nextBtn.classList.remove('opacity-40', 'cursor-not-allowed');
                }
            }
        }

        // Initial state
        updateSlider(0);

        // Button listeners
        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                if (currentIndex > 0) updateSlider(currentIndex - 1);
            });
        }
        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                if (currentIndex < totalScreens - 1) updateSlider(currentIndex + 1);
            });
        }

        // Dot listeners
        dots.forEach(dot => {
            dot.addEventListener('click', (e) => {
                const targetIdx = parseInt(e.currentTarget.getAttribute('data-index'), 10);
                updateSlider(targetIdx);
            });
        });

        // Keyboard Accessibility
        container.setAttribute('tabindex', '0');
        container.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowLeft') {
                if (currentIndex > 0) updateSlider(currentIndex - 1);
            } else if (e.key === 'ArrowRight') {
                if (currentIndex < totalScreens - 1) updateSlider(currentIndex + 1);
            }
        });

        // Touch swipe support
        let startX = 0;
        let isDragging = false;

        container.addEventListener('touchstart', (e) => {
            startX = e.touches[0].clientX;
            isDragging = true;
        }, { passive: true });

        container.addEventListener('touchend', (e) => {
            if (!isDragging) return;
            isDragging = false;
            const endX = e.changedTouches[0].clientX;
            const diffX = endX - startX;

            if (diffX < -40 && currentIndex < totalScreens - 1) {
                updateSlider(currentIndex + 1);
            } else if (diffX > 40 && currentIndex > 0) {
                updateSlider(currentIndex - 1);
            }
        });
    }

    // 8. Portfolio Category Filter Tabs
    const portfolioTabs = document.querySelectorAll('[data-portfolio-filter]');
    const portfolioItems = document.querySelectorAll('[data-portfolio-category]');

    if (portfolioTabs.length > 0) {
        portfolioTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                const filter = tab.getAttribute('data-portfolio-filter');

                portfolioTabs.forEach(t => {
                    t.classList.remove('bg-white', 'text-black', 'border-white');
                    t.classList.add('bg-zinc-900', 'text-zinc-400', 'border-zinc-800');
                    t.setAttribute('aria-selected', 'false');
                });
                tab.classList.remove('bg-zinc-900', 'text-zinc-400', 'border-zinc-800');
                tab.classList.add('bg-white', 'text-black', 'border-white');
                tab.setAttribute('aria-selected', 'true');

                portfolioItems.forEach(item => {
                    const itemCat = item.getAttribute('data-portfolio-category');
                    if (filter === 'all' || (itemCat && itemCat.includes(filter))) {
                        item.classList.remove('hidden');
                    } else {
                        item.classList.add('hidden');
                    }
                });
            });
        });
    }

    // 9. Exclusive Audio Playback (pause others when one starts)
    const audioElements = document.querySelectorAll('audio');
    audioElements.forEach(audio => {
        audio.addEventListener('play', () => {
            audioElements.forEach(other => {
                if (other !== audio && !other.paused) {
                    other.pause();
                }
            });
        });
    });

    // 10. Contact Form Logic (EmailJS with fallback)
    const contactForm = document.getElementById("contact-form");
    const statusMessage = document.getElementById("status-message");

    if (contactForm) {
        if (typeof emailjs !== 'undefined') {
            try {
                emailjs.init("KhhpDMoVBpGtqgSjM");
            } catch (err) {
                console.warn("EmailJS init warning:", err);
            }
        }

        contactForm.addEventListener("submit", async (event) => {
            event.preventDefault();
            const form = event.target;
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn ? submitBtn.innerHTML : 'WYŚLIJ WIADOMOŚĆ';
            
            if (submitBtn) {
                submitBtn.innerHTML = 'WYSYŁANIE...';
                submitBtn.disabled = true;
            }
            if (statusMessage) {
                statusMessage.textContent = "Wysyłanie wiadomości...";
                statusMessage.className = "mt-4 text-center text-sm text-zinc-400";
            }

            // Collect form fields
            const name    = form.querySelector('[name="from_name"]')?.value?.trim() || '';
            const email   = form.querySelector('[name="reply_to"]')?.value?.trim() || '';
            const message = form.querySelector('[name="message"]')?.value?.trim() || '';

            try {
                if (typeof emailjs !== 'undefined') {
                    await emailjs.send(
                        "service_kf463es",
                        "template_q83n3iv",
                        {
                            from_name: name,
                            reply_to:  email,
                            message:   message,
                        }
                    );
                    form.reset();
                    if (statusMessage) {
                        statusMessage.textContent = "Dziękujemy! Twoja wiadomość została wysłana. Odezwiemy się wkrótce.";
                        statusMessage.className = "mt-4 text-center text-sm text-green-400";
                    }
                } else {
                    // Fallback mailto
                    const subject = encodeURIComponent(`Wiadomość od ${name}`);
                    const body    = encodeURIComponent(`Od: ${name} (${email})\n\n${message}`);
                    window.location.href = `mailto:contact@4noxwav.com?subject=${subject}&body=${body}`;

                    if (statusMessage) {
                        statusMessage.textContent = "Otwieram program pocztowy z Twoją wiadomością...";
                        statusMessage.className = "mt-4 text-center text-sm text-zinc-300";
                    }
                }
            } catch (error) {
                console.error("Failed to send message:", error);
                if (statusMessage) {
                    statusMessage.textContent = "Wystąpił błąd podczas wysyłania. Napisz bezpośrednio na contact@4noxwav.com";
                    statusMessage.className = "mt-4 text-center text-sm text-red-400";
                }
            } finally {
                if (submitBtn) {
                    submitBtn.innerHTML = originalBtnText;
                    submitBtn.disabled = false;
                }
            }
        });
    }
});

// Global copy to clipboard function
window.copyEmail = function(email, element, isText = false) {
    if (!navigator.clipboard) {
        const tempInput = document.createElement('input');
        tempInput.value = email;
        document.body.appendChild(tempInput);
        tempInput.select();
        document.execCommand('copy');
        document.body.removeChild(tempInput);
        showFeedback(element, isText);
        return;
    }

    navigator.clipboard.writeText(email).then(() => {
        showFeedback(element, isText);
    }).catch(err => {
        console.error('Failed to copy text: ', err);
    });
};

function showFeedback(element, isText) {
    const originalHtml = element.innerHTML;
    if (isText) {
        element.innerHTML = 'Skopiowano!';
    } else {
        element.innerHTML = '<span class="font-bold text-xs">✓ Skopiowano</span>';
    }
    
    setTimeout(() => {
        element.innerHTML = originalHtml;
    }, 2000);
}
