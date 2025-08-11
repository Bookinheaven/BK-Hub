document.addEventListener("DOMContentLoaded", () => {

    let data = [
        {
            "id": "basic-1",
            "title": "Fade Animation",
            "path": "./basics/fade/fade.html",
            "des": "Concept: Use CSS opacity and transition"
        },
        {
            "id": "basic-2",
            "title": "Slide Animation",
            "path": "./basics/slide/slide.html",
            "des": "Concept: Use CSS opacity and transition"
        }
    ];
    
    data.forEach(({id, title, path, des}) => {
        const sectionHTML = `
            <section id="${id}" class="section">
            <div class="header-wrapper">
                <div class="header">
                <h1>${title}</h1>
                </div>
                <div class="header-slide">
                <p>${des}</p>
                </div>
            </div>
            <iframe class="frame" src="${path}"></iframe>
            </section>
        `;
        document.body.insertAdjacentHTML('beforeend', sectionHTML);
        const line1 = `<li><a href="#${id}">${title}</a></li>`;  // removed inline onclick
        document.getElementsByClassName("sublist")[0].insertAdjacentHTML("beforeend", line1);
    });

    let sections = document.querySelectorAll(".section");

    const scrollObserver = new IntersectionObserver(function (entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                document.querySelectorAll('.sublist a').forEach(a => a.classList.remove('active'));
                const activeLink = document.querySelector(`.sublist a[href="#${entry.target.id}"]`);
                if (activeLink) activeLink.classList.add('active');
            }
        });
    }, { root: null, threshold: 0.2, rootMargin: "0px" });

    sections.forEach(entry => {
        if (entry.id != "indexer"){
            entry.children[0].addEventListener('mouseenter', () => {
                entry.children[0].children[1].classList.add("show");
            });

            entry.children[0].addEventListener('mouseleave', () => {
                entry.children[0].children[1].classList.remove("show");
            });
        }
        scrollObserver.observe(entry);
    });

    document.querySelectorAll('.sublist a').forEach(link => {
        link.addEventListener('click', e => {
            e.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const target = document.getElementById(targetId);
            if(target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        });
    });

    const toggleBtn = document.querySelector('.toggle-sublist');
    if (toggleBtn) {
        toggleBtn.addEventListener('click', function () {
            const sublist = document.querySelector('.sublist');
            const arrow = this.textContent.includes('▸') ? '▾' : '▸';
            sublist.style.display = sublist.style.display === 'none' ? 'block' : 'none';
            this.textContent = `Basics ${arrow}`;
        });
    }
});
