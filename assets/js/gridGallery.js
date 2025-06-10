const images = [
  { source: "imgs/prompts/meme_1.png", description: "North Korea" },
  { source: "imgs/prompts/meme_3.png", description: "South Korea" },
  { source: "imgs/prompts/meme_2.png", description: "Brazil" },
  { source: "imgs/prompts/meme_4.png", description: "Portugal" },
  { source: "imgs/prompts/meme_9.png", description: "USA + pop" },
  { source: "imgs/prompts/meme_10.png", description: "USA + republican" },
  { source: "imgs/prompts/meme_11.png", description: "Burkina Faso" },
  { source: "imgs/prompts/meme_12.png", description: "Greenland" },
  { source: "imgs/prompts/meme_13.png", description: "Georgia" },
  { source: "imgs/prompts/meme_14.png", description: "Papua New Guinea" },
  {source: "imgs/prompts/meme_15.png", description: "Saint Tomé and Principe",},
  { source: "imgs/prompts/meme_16.png", description: "Mozambique" },
  { source: "imgs/prompts/meme_17.png", description: "Paraguay" },
  { source: "imgs/prompts/meme_18.png", description: "Chile" },
  { source: "imgs/prompts/meme_19.png", description: "Lebanon" },
  { source: "imgs/prompts/meme_20.png", description: "Tuvalu" },
  { source: "imgs/prompts/meme_21.png", description: "Montenegro" },
  { source: "imgs/prompts/meme_22.png", description: "Tajikistan" },
  { source: "imgs/prompts/meme_23.png", description: "Mapuche (Chile)" },
  { source: "imgs/prompts/meme_24.png", description: "prompt 20" },
  { source: "imgs/prompts/meme_25.png", description: "Basotho (Lesotho)" },
  { source: "imgs/prompts/meme_26.png", description: "Kurdistan" },
  { source: "imgs/prompts/meme_27.png", description: "Guaraní" },
  { source: "imgs/prompts/meme_28.png", description: "Yakut" },
  { source: "imgs/prompts/meme_29.png", description: "Transinistra" },
  { source: "imgs/prompts/meme_30.png", description: "Oman" },
  { source: "imgs/prompts/meme_31.png", description: "Uganda" },
];

const srcSelect = () => {
  const imgInfo = document.querySelector("#modal-src");
  const imgDescription = document.querySelector("#modal-desc");
  const galeria = document.querySelector(".galeria");

  galeria.addEventListener("click", function (e) {
    const children = Array.from(galeria.children);
    const clicked = e.target.closest(".modal-image-source");

    if (!clicked || !galeria.contains(clicked)) return;

    const index = children.indexOf(clicked);

    imgInfo.src = `../../${images[index].source}`;
    imgDescription.innerHTML = `${images[index].description}`;
  });
};

srcSelect();

const imageShow = () => {
  const ventana = document.querySelector(".modal");
  ventana.style.top = 0;
  ventana.style.transition = "top 1.5s";
};

const closeWindow = () => {
  const closeVentana = document.querySelector("#moda-image-button");
  const ventana = document.querySelector(".modal");
  ventana.style.top = "-100%";
};
