<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0b1020,100:2563eb&height=200&section=header&text=Luis%20Santos&fontSize=58&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Ingeniero%20de%20Software%20Full-Stack&descAlignY=60&descSize=20" alt="Luis Santos" width="100%"/>

<a href="https://github.com/SaintsLuis">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=22&pause=1200&color=3B82F6&center=true&vCenter=true&width=640&lines=%C2%A1Hola%2C+soy+Luis+Santos!+%F0%9F%91%8B;Ingeniero+de+Software+Full-Stack;Web+%2B+M%C3%B3vil+%2B+SaaS;NestJS+%C2%B7+React+%C2%B7+Next.js+%C2%B7+TypeScript;Siempre+aprendiendo+tecnolog%C3%ADas+nuevas" alt="Typing SVG" />
</a>

<br/>

<a href="https://santosvluis.vercel.app"><img src="https://img.shields.io/badge/Portafolio-santosvluis.vercel.app-2563eb?style=for-the-badge&logo=vercel&logoColor=white" alt="Portafolio"/></a>
<a href="https://www.linkedin.com/in/santosvluis/"><img src="https://img.shields.io/badge/LinkedIn-santosvluis-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="mailto:santosvluism@gmail.com"><img src="https://img.shields.io/badge/Email-Cont%C3%A1ctame-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>

<br/><br/>

<img src="https://komarev.com/ghpvc/?username=SaintsLuis&label=Visitas&color=2563eb&style=flat-square" alt="Visitas al perfil"/>

</div>

---

## 👨‍💻 Sobre mí

```ts
const luis = {
  rol: "Ingeniero de Software Full-Stack",
  ubicacion: "Santo Domingo, República Dominicana 🇩🇴",
  idiomas: ["Español"],
  trabajoCon: ["Web", "Móvil", "SaaS"],
  principios: ["Clean Architecture", "DDD", "Código mantenible y probado"],
  abiertoA: "Oportunidades full-stack: remoto, híbrido o en Santo Domingo",
  siempre: "Aprendiendo tecnologías nuevas",
};
```

---

## 🛠️ Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=ts,js,react,nextjs,angular,nodejs,nestjs,cs,dotnet&perline=9" alt="Lenguajes y frameworks"/>
<br/>
<img src="https://skillicons.dev/icons?i=postgres,mongodb,prisma,docker,tailwind,astro,git&perline=7" alt="Datos y herramientas"/>

</div>

---

## 🚀 Proyectos principales

> Despliega cada proyecto para ver más detalles 👇 · Más en mi [portafolio](https://santosvluis.vercel.app)

<details>
<summary><b>🏥 Medical Date</b> — plataforma médica completa (API + web + móvil)</summary>
<br/>

Los pacientes agendan citas desde el celular; médicos y secretarías gestionan citas, historiales, recetas y facturación, con permisos por rol.

- **Demo:** [medical-date-landing-page.vercel.app](https://medical-date-landing-page.vercel.app)
- **Código:** [frontend](https://github.com/SaintsLuis/medical-date_frontend) · [landing page](https://github.com/SaintsLuis/medical-date_landing-page)
- **Stack:** Next.js · React Native · NestJS · PostgreSQL · Prisma · Docker

</details>

<details>
<summary><b>💼 CarteraGo</b> — reemplaza el cuaderno de un prestamista</summary>
<br/>

Los cobradores registran pagos desde el celular, el dueño los ve al instante y el cierre diario cuadra automáticamente.

- **Demo:** [carterago.vercel.app](https://carterago.vercel.app)

</details>

<details>
<summary><b>🍽️ Brasa &amp; Co.</b> — kiosco de autoservicio para restaurantes</summary>
<br/>

El cliente pide, personaliza y paga en pantalla; la cocina recibe el pedido de inmediato. El servidor recalcula los precios, así que los totales no se pueden manipular desde el cliente.

- **Código:** [restaurant-kiosk](https://github.com/SaintsLuis/restaurant-kiosk)

</details>

<details>
<summary><b>🛍️ Teslo Shop</b> — tienda en línea de punta a punta</summary>
<br/>

Búsqueda, carrito, cuentas de usuario, pagos con PayPal y panel de administración para productos y pedidos.

- **Demo:** [teslo-shop-lms.vercel.app](https://teslo-shop-lms.vercel.app)

</details>

---

## 🧠 Cómo trabajo

Me gusta construir apps que sigan siendo fáciles de cambiar cuando crecen. Mi forma de pensarlas:

1. **Primero el negocio, después la tecnología.** Modelo el dominio (citas, pagos, cierres de caja) con DDD antes de elegir herramientas.
2. **Clean Architecture.** Las reglas del negocio no dependen del framework ni de la base de datos: las dependencias apuntan hacia adentro. Si cambia el proveedor de pagos o la base de datos, el núcleo no se reescribe.
3. **El servidor es la fuente de verdad.** Validaciones, permisos y cálculos (como los precios del kiosco) viven en el backend, no en el cliente.
4. **Un backend, varios clientes.** Una misma API alimenta el panel web y la app móvil, así las reglas no se duplican.
5. **SOLID y módulos pequeños.** Cada módulo hace una cosa, se puede probar solo y se puede crecer sin romper lo demás.
6. **Entornos reproducibles.** Docker y migraciones versionadas para que levantar el proyecto sea igual en cualquier máquina.

```mermaid
flowchart LR
    W[Web · Next.js] --> A
    M[Móvil · React Native] --> A
    A[API · NestJS] --> C[Casos de uso]
    C --> D((Dominio))
    I[Infraestructura<br/>PostgreSQL · Prisma · Pagos] --> D
```

---

## 📊 Estadísticas de GitHub

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=SaintsLuis&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0b1020" alt="Estadísticas de GitHub"/>
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=SaintsLuis&layout=compact&theme=tokyonight&hide_border=true&bg_color=0b1020" alt="Lenguajes más usados"/>

<br/>

<img src="https://streak-stats.demolab.com?user=SaintsLuis&theme=tokyonight&hide_border=true&background=0b1020" alt="Racha de contribuciones"/>

</div>

---

<div align="center">

### 📫 ¿Hablamos?

Estoy abierto a oportunidades como desarrollador full-stack.
Escríbeme por [LinkedIn](https://www.linkedin.com/in/santosvluis/) o a [santosvluism@gmail.com](mailto:santosvluism@gmail.com).

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2563eb,100:0b1020&height=100&section=footer" width="100%" alt=""/>

</div>
