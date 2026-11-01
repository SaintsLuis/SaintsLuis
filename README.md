<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0b1020,100:2563eb&height=200&section=header&text=Luis%20Santos&fontSize=58&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Full-Stack%20Software%20Engineer&descAlignY=60&descSize=20" alt="Luis Santos" width="100%"/>

<a href="https://github.com/SaintsLuis">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=22&pause=1200&color=3B82F6&center=true&vCenter=true&width=640&lines=Hi%2C+I'm+Luis+Santos+%F0%9F%91%8B;Full-Stack+Software+Engineer;Web+%2B+Mobile+%2B+SaaS;NestJS+%C2%B7+React+%C2%B7+Next.js+%C2%B7+TypeScript;Always+learning+new+technologies" alt="Typing SVG" />
</a>

<br/>

<a href="https://santosvluis.vercel.app"><img src="https://img.shields.io/badge/Portfolio-santosvluis.vercel.app-2563eb?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio"/></a>
<a href="https://www.linkedin.com/in/santosvluis/"><img src="https://img.shields.io/badge/LinkedIn-santosvluis-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="mailto:santosvluism@gmail.com"><img src="https://img.shields.io/badge/Email-Get%20in%20touch-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>

<br/><br/>

<img src="https://komarev.com/ghpvc/?username=SaintsLuis&label=Profile%20views&color=2563eb&style=flat-square" alt="Profile views"/>

</div>

---

## 👨‍💻 About me

```ts
const luis = {
  role: "Full-Stack Software Engineer",
  location: "Santo Domingo, Dominican Republic 🇩🇴",
  languages: ["Spanish", "English"],
  buildsWith: ["Web", "Mobile", "SaaS"],
  principles: ["Clean Architecture", "DDD", "Maintainable, well-tested code"],
  openTo: "Full-stack roles: remote, hybrid or in Santo Domingo",
  always: "Learning new technologies",
};
```

---

## 🛠️ Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=ts,js,react,nextjs,angular,nodejs,nestjs,cs,dotnet&perline=9" alt="Languages and frameworks"/>
<br/>
<img src="https://skillicons.dev/icons?i=postgres,prisma,supabase,docker,aws,vercel,tailwind,astro,git&perline=9" alt="Data and tooling"/>

</div>

---

## 🚀 Featured projects

> Expand each project to see screenshots and details 👇 · More work in my [portfolio](https://santosvluis.vercel.app)

<details open>
<summary><b>🏥 Medical Date</b> — complete medical platform (API + web + mobile)</summary>
<br/>

Patients book appointments from their phone; doctors and secretaries manage appointments, medical records, prescriptions and billing, with role-based permissions.

<img src="https://santosvluis.vercel.app/shots/medical-date-landing.webp" alt="Medical Date landing page" width="100%"/>

- **Live:** [medical-date-landing-page.vercel.app](https://medical-date-landing-page.vercel.app)
- **Code:** [frontend](https://github.com/SaintsLuis/medical-date_frontend) · [landing page](https://github.com/SaintsLuis/medical-date_landing-page)
- **Stack:** Next.js · React Native · NestJS · PostgreSQL · Prisma · Docker

</details>

<details>
<summary><b>💼 CarteraGo</b> — replaces a lender's paper ledger</summary>
<br/>

Collectors log payments from their phone, the owner sees them instantly, and daily closing balances automatically.

<img src="https://santosvluis.vercel.app/shots/carterago/dashboard.webp" alt="CarteraGo dashboard" width="49%"/>
<img src="https://santosvluis.vercel.app/shots/carterago/ruta-hoy.webp" alt="CarteraGo daily route" width="49%"/>

- **Live:** [carterago.vercel.app](https://carterago.vercel.app)

</details>

<details>
<summary><b>🍽️ Brasa &amp; Co.</b> — self-service kiosk for restaurants</summary>
<br/>

Customers order, customize and pay on screen, and the kitchen receives the order immediately. The server recalculates prices, so totals can't be tampered with from the client.

<img src="https://santosvluis.vercel.app/shots/kiosk/menu.webp" alt="Brasa &amp; Co. menu screen" width="49%"/>
<img src="https://santosvluis.vercel.app/shots/kiosk/cocina.webp" alt="Brasa &amp; Co. kitchen screen" width="49%"/>

- **Code:** [restaurant-kiosk](https://github.com/SaintsLuis/restaurant-kiosk)

</details>

<details>
<summary><b>🛍️ Teslo Shop</b> — end-to-end online store</summary>
<br/>

Search, cart, user accounts, PayPal payments, and an admin panel for products and orders.

<img src="https://santosvluis.vercel.app/shots/teslo/inicio.webp" alt="Teslo Shop home" width="49%"/>
<img src="https://santosvluis.vercel.app/shots/teslo/producto.webp" alt="Teslo Shop product page" width="49%"/>

- **Live:** [teslo-shop-lms.vercel.app](https://teslo-shop-lms.vercel.app)

</details>

## 🧠 How I work

I like building apps that stay easy to change as they grow. This is how I approach them:

1. **Business first, technology second.** I model the domain (appointments, payments, daily closings) with DDD before choosing tools.
2. **Clean Architecture.** Business rules don't depend on the framework or the database: dependencies point inward. If the payment provider or the database changes, the core isn't rewritten.
3. **The server is the source of truth.** Validation, permissions and calculations (like the kiosk's prices) live in the backend, not in the client.
4. **One backend, many clients.** A single API feeds the web dashboard and the mobile app, so rules are never duplicated.
5. **SOLID and small modules.** Each module does one thing, can be tested on its own, and can grow without breaking the rest.
6. **Reproducible environments.** Docker and versioned migrations, so the project runs the same on any machine.

```mermaid
flowchart LR
    W[Web · Next.js] --> A
    M[Mobile · React Native] --> A
    A[API · NestJS] --> C[Use cases]
    C --> D((Domain))
    I[Infrastructure<br/>PostgreSQL · Prisma · Payments] --> D
```

---

---

## 📊 GitHub stats

<!--START_STATS-->
<div align="center">

| 📦 Repos | ⭐ Stars | 👥 Followers | 🔥 Contributions (last year) | ⚡ Streak | 🏆 Best streak |
|:-:|:-:|:-:|:-:|:-:|:-:|
| **29** | **6** | **5** | **53** | **1 day** | **2 days** |

**Top languages:** TypeScript **73%** · JavaScript **10%** · HTML **5%** · C# **4%** · Astro **4%**

<sub>Updated automatically on 2026-11-01.</sub>

</div>
<!--END_STATS-->

---

<div align="center">

### 📫 Let's talk

I'm open to full-stack opportunities.
Reach me on [LinkedIn](https://www.linkedin.com/in/santosvluis/) or at [santosvluism@gmail.com](mailto:santosvluism@gmail.com).

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2563eb,100:0b1020&height=100&section=footer" width="100%" alt=""/>

</div>
