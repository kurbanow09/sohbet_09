document.addEventListener('DOMContentLoaded', function() {
    // Hamburger menü toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('nav ul');
    
    hamburger.addEventListener('click', function() {
        this.classList.toggle('active');
        navLinks.classList.toggle('active');
    });

    // Nav linklerine tıklama
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            // Mobilde menüyü kapat
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
            
            // Scroll animasyonu
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            window.scrollTo({
                top: targetSection.offsetTop - 100,
                behavior: 'smooth'
            });
        });
    });

    // Matrix arka plan efekti
    function createMatrixEffect() {
        const matrixBg = document.querySelector('.matrix-bg');
        const svgStrings = [];
        
        for (let i = 0; i < 1000; i++) {
            const x = Math.floor(Math.random() * 100);
            const y = Math.floor(Math.random() * 100);
            svgStrings.push(`<rect width="1" height="1" x="${x}" y="${y}"/>`);
        }
        
        matrixBg.style.backgroundImage = 
            `linear-gradient(rgba(13, 13, 13, 0.9), rgba(13, 13, 13, 0.9)),
            url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="%2300ff4133">${svgStrings.join('')}</svg>')`;
    }

    createMatrixEffect();

    // Kod bloklarına vurgulama ekleme
    document.querySelectorAll('pre code').forEach(block => {
        // HTML vurgulama
        if (block.classList.contains('language-html')) {
            const html = block.innerHTML;
            const highlighted = html
                .replace(/&lt;(\/?)(\w+)([^&]*)&gt;/g, 
                    '&lt;<span class="tag">$1$2</span>$3&gt;')
                .replace(/(\w+)=/g, '<span class="attr">$1</span>=')
                .replace(/&quot;([^&]*)&quot;/g, '&quot;<span class="val">$1</span>&quot;');
            block.innerHTML = highlighted;
        }
        
        // CSS vurgulama
        if (block.classList.contains('language-css')) {
            const css = block.innerHTML;
            const highlighted = css
                .replace(/([^{}]+)\s*{/g, '<span class="sel">$1</span>{')
                .replace(/([a-z-]+)\s*:/g, '<span class="prop">$1</span>:')
                .replace(/:\s*([^;}]+)/g, ': <span class="val">$1</span>')
                .replace(/[{};]/g, '<span class="punc">$&</span>');
            block.innerHTML = highlighted;
        }
    });
});