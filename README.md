# HACKING-THE-HUMAN-VASCULATURE-
The intricate web of cellular interactions, spatial organization, and specialization within the human body, boasting a staggering 37 trillion cells, propels the motivation for this project. Reseachers grapple with understanding these complex cellular functions and relationships through the Vasculature Common Coordinate Framework (VCCF). This framework utilizes the blood vasculature as a primary navigation system, employing capillary structures as unique addresses to map cellular locations across all scale levels.
 
 ![image](https://github.com/kimo944/HACKING-THE-HUMAN-VASCULATURE-/assets/134097491/f31154da-494b-4401-b6ee-e766d5aa5f9e)

In light of gaps in researchers' knowledge about the vasculature that translate into gaps within the VCCF, the motivation to introduce data science into this framework is clear. The potential to automatically segment vasculature arrangements, harnessing real-world tissue data, becomes a crucial pursuit to bridge existing gaps and offer a comprehensive understanding of the vasculature throughout the entire human body.
The current manual annotation process, conducted by human expert annotators, is painstakingly slow, with each new dataset demanding over six months for completion. Machine learning approaches face challenges in adapting to new datasets due to the inherent variability in human anatomy and the evolving image quality associated with HiP-CT technology.
The overarching motivation is amplified by the goal of the competition hosted by the Common Fund’s Cellular Senescence Network (SenNet) Program. This program aims to systematically identify and characterize differences in senescent cells across various states of human health, the entire lifespan, and diverse parts of the body. SenNet not only provides publicly accessible atlases of senescent cells but also pioneers innovative tools building upon advancements in single-cell analysis.


![image](https://github.com/kimo944/HACKING-THE-HUMAN-VASCULATURE-/assets/134097491/b13d62ad-81aa-410d-b035-8c36b80d9310)

 
Figure [2]- Human Reference Atlas Charts Human Body at Single Cell Level

Collaborating with SenNet, the Human Organ Atlas (HOA) introduces an additional layer of motivation. HOA, with its 3D multi-resolution imaging datasets created through HiP-CT at the European Synchrotron Radiation Facility, delves into a scale in human anatomy that was previously poorly understood—ranging from microns to entire intact organs.
In essence, this project aspires to advance our understanding of how vasculature influences different cells in the human body. Enhanced data could pave the way for simulations of blood, oxygen, or drug flow through the vessel network. Additionally, organ images may provide valuable insights into how blood vasculature changes with variations in sex, age, and BMI. Ultimately, the project aims to contribute to the development of a more comprehensive Vascular Common Coordinate Framework (VCCF) and Human Reference Atlas (HRA), unraveling the intricate relationships between cells and their profound implications for human health.




![image](https://github.com/kimo944/HACKING-THE-HUMAN-VASCULATURE-/assets/134097491/b4e6e691-63d9-4a59-a8bb-c8a348701fc0)



1.3	SCOPE OF WORK
The project aims to develop a model for segmenting blood vessels using 3D Hierarchical Phase-Contrast Tomography (HiP-CT) data acquired from human kidneys. The goal of this model is to enhance researchers' understanding of the size, shape, branching angles, and overall patterning of blood vessels in human tissues.


1.4	IMPORTANCE OF THE WORK

Completing the Vasculature Picture: The project seeks to fill gaps in understanding 
blood vessels throughout the human body by applying 3D analysis techniques to HiP-CT
data. Analysis of Vessel Size and Shape: The model provides an opportunity to explore variations
in the size and shape of blood vessels.
Enhancing Understanding of Branching and Patterns: The work contributes to a better understanding
of branching angles and overall patterns of blood vessels in human tissues.

1.5	EXPECTED IMPACT

Scientific Advancement: The model contributes to scientific knowledge by providing an accurate
and detailed representation of blood vessels. Improved Medical Applications: It supports in-depth medical understanding of blood vessels, potentially aiding in diagnostics and treatment planning.
HiP-CT Technology Validation: The work helps validate the effectiveness of HiP-CT technology in precisely studying blood vessels.

1.6	ANTICIPATED CHALLENGES

Variability in Human Anatomy: Addressing challenges arising from natural variability
in human anatomy to ensure the model's adaptability to different individuals.
Changes in Image Quality: Tackling issues related to changes in image quality, 
Adapting the model to variations in HiP-CT technology.

1.7	PROBLEM STATEMENT

The intricate network of cellular interactions within the human body, consisting of approximately 37 trillion cells, presents a formidable challenge for researchers seeking a comprehensive understanding of spatial organization, specialization, and the influence of blood vasculature. The Vasculature Common Coordinate Framework (VCCF) serves as a crucial tool, utilizing the blood vasculature as a navigational system to map cellular locations across various scales. However, significant gaps persist in our knowledge of the vasculature, translating into limitations within the VCCF, hindering a thorough comprehension of cellular functions and relationships.
A primary obstacle arises from the labor-intensive and time-consuming manual annotation process currently employed. Expert annotators spend over six months annotating each new dataset, impeding the pace of research and hindering the scalability of the VCCF. Furthermore, the inherent variability in human anatomy and the evolving image quality associated with Hierarchical Phase-Contrast Tomography (HiP-CT) pose challenges for machine learning approaches attempting to adapt consistently across diverse datasets.
The urgency to address these challenges is underscored by the objectives of the Common Fund’s Cellular Senescence Network (SenNet) Program, which seeks to systematically identify and characterize senescent cells throughout various states of human health, the entire lifespan, and diverse body parts. Collaborating with SenNet and the Human Organ Atlas (HOA), which utilizes 3D multi-resolution imaging datasets, amplifies the significance of the project. The overarching goal is to advance our understanding of how blood vasculature influences different cells, potentially leading to breakthroughs in simulating blood flow, oxygen distribution, and drug transport through the vessel network.
In response to these challenges, there is a critical need to integrate data science into the VCCF framework, automating the segmentation of vasculature arrangements in HiP-CT data. This automation aims to bridge existing gaps, streamline the annotation process, and contribute to the development of a more comprehensive Vascular Common Coordinate Framework (VCCF) and Human Reference Atlas (HRA). 


![image](https://github.com/kimo944/HACKING-THE-HUMAN-VASCULATURE-/assets/134097491/bb786a56-ff5b-460e-bbac-480d2c0a322e)


1.8	PROBLEM REQUIREMENTS
Our project revolves around addressing specific requirements to effectively resolve the outlined challenges:

Data Segmentation Model: We aim to develop a robust model capable of accurately segmenting blood vessels in 3D HiP-CT data, a crucial step in overcoming the limitations in understanding the vasculature.
Adaptability: It is imperative that our model demonstrates adaptability to different individuals, addressing the inherent variability in human anatomy. This adaptability is key to ensuring consistent segmentation across diverse datasets.
Image Quality Management: Our approach involves addressing issues related to changes in image quality, allowing the model to seamlessly adapt to variations in HiP-CT technology and ensuring accurate segmentation.
Automation: Our strategy is to integrate data science into the VCCF framework to automate the segmentation of vasculature arrangements in HiP-CT data. This automation aims to streamline the annotation process and contribute to the development of a more comprehensive Vascular Common Coordinate Framework (VCCF) and Human Reference Atlas (HRA).
Collaborative Approach: We seek to collaborate effectively with SenNet and HOA, leveraging their datasets and insights to contribute to a more comprehensive understanding of vascular structures.
