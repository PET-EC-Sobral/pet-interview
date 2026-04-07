<div align="center">

# PET Interview - Grupo de Estudos para Entrevistas Técnicas de Programação

<img src="./assets/PET-INTERVIEW_FULL-LOGO.png" alt="PET Interview Logo" width="200"/>

<p>
    <a href="https://petec.ufc.br/pt/">
        <img src="https://img.shields.io/badge/Programa%20de%20Educa%C3%A7%C3%A3o%20Tutorial%20(PETEC)%20-%20E?style=for-the-badge&color=%23137EE2&link=https%3A%2F%2Fpetec.ufc.br%2Fpt%2F" alt="Programa de Educacao Tutorial - PETEC" />
    </a>
    <a href="https://sobral.ufc.br/">
        <img src="https://img.shields.io/badge/Universidade%20Federal%20Do%20Cear%C3%A1%20(UFC)%20Sobral%20-%20%23008F36?style=for-the-badge&link=https%3A%2F%2Fsobral.ufc.br%2F" alt="Universidade Federal do Ceara (UFC) Sobral" />
    </a>
</p>

### O **PET Interview** é um grupo de estudos focado em preparar estudantes da UFC Sobral para os desafios técnicos de processos seletivos em grandes empresas de tecnologia (Big Techs). Nosso objetivo é preencher a lacuna entre o conhecimento acadêmico e as exigências práticas das entrevistas, focando no que realmente importa para conquistar a vaga.

</div>

## 🎯 Objetivos do Projeto

- **Fundamentos Sólidos:** Praticar algoritmos e estruturas de dados (o "feijão com arroz" da computação).
- **Raciocínio Lógico:** Desenvolver a capacidade de decompor problemas complexos em soluções eficientes.
- **Comunicação Técnica:** Aprender a explicar o raciocínio por trás do código, habilidade essencial na era da I.A.
- **Colaboração:** Evoluir em conjunto, revisando soluções e compartilhando diferentes abordagens para o mesmo problema.

---

## 📂 Estrutura de Pastas

Para manter o repositório organizado e facilitar a busca por soluções específicas, adotamos uma hierarquia rígida de diretórios. Ao adicionar sua contribuição, siga este modelo:

```text
challenges/
└── <nome-da-plataforma>/           # leetcode, beecrowd, neetcode, outros...
    └── <id>: <nome-do-desafio>/    # Ex: "01: Two Sum" ou "1001: Extremamente Básico"
        └── <linguagem>/            # python, cpp, java, typescript, etc.
            └── <numero-solucao>/   # 01, 02, 03... (para diferentes métodos/membros)
                ├── solucao.ext     # Arquivo de código-fonte
                ├── README.md       # Explicação da lógica (opcional)
                └── assets/         # Imagens ou prints relacionados (opcional)
```

---

## 🚀 Como Contribuir

Para manter o repositório "limpo" e padronizado, siga os passos abaixo para enviar seu código:

### 1\. Preparação

Certifique-se de que seu arquivo de código segue as regras do nosso `.gitignore` (não envie executáveis, apenas o código-fonte).

### 2\. Criando a Estrutura

Se o desafio que você resolveu ainda não existe no repositório:

1.  Navegue até a pasta `challenges/`.
2.  Identifique a plataforma (ou crie a pasta, se for nova).
3.  Crie a pasta do desafio seguindo o padrão `<numero-identificador>: <Nome do Desafio>`.
4.  Dentro dela, crie a pasta da linguagem utilizada e, por fim, a pasta da sua solução (ex: `01`).

### 3\. O que enviar?

- **Código-Fonte:** O arquivo principal da solução organizado e devidamente comentado (ex: `main.py`, `solution.cpp`).
- **Documentação (Opcional):** Um arquivo `.md` ou `.txt` explicando a complexidade de tempo/espaço ($O(n)$, $O(\log n)$, etc.) ou links que te ajudaram a resolver.
- **Mídia (Opcional):** Prints de submissão aceita ou diagramas da lógica na pasta `assets/`.

### 4\. Exemplo Prático

Se você resolveu o desafio "Two Sum" do LeetCode em Python e é a primeira solução do grupo:
`challenges/leetcode/1: Two Sum/python/01/solution.py`

---

## 🛠️ Regras de Padronização

- **Quebras de Linha:** O repositório está configurado para usar o padrão **LF** (Linux). Se você usa Windows, o Git fará a conversão automática graças ao nosso `.gitattributes`.
- **Nomenclatura:** Evite espaços desnecessários em nomes de arquivos, mas sinta-se livre para usar espaços no nome da pasta do desafio para manter a legibilidade.
- **Qualidade:** Comente partes complexas do seu código para ajudar os outros membros no aprendizado.

---

## 🤝 Organizadores

Este projeto foi desenvolvido pelo **Programa de Educação Tutorial (PET)** - programa formado por um grupo de discentes do curso de Engenharia de Computação da UFC Sobral.

### Equipe de organização do PET Interview:

- [Cizé Lucas](https://github.com/CizeLucas)
- [Pâmela Maria](https://github.com/P4m3l4m4r14)
- [Vitória Emilly](https://github.com/vitsantos)

### Agradecimentos

- Ideia inicial que originou o grupo e Mentorias do [Henrique Vasconcelos](https://www.linkedin.com/in/henriquehsv/)
- Tutoria PET do [Prof. Dr. Wendley S. Silva](https://ec.ufc.br/pt/wendley/)
- Universidade Federal do Ceará - Campus Sobral

---

<br>

# English Version

### **PET Interview** is a study group focused on preparing UFC Sobral students for the technical challenges of selection processes at major technology companies (Big Techs). Our goal is to bridge the gap between academic knowledge and the practical demands of interviews, focusing on what really matters to secure the job.

## 🎯 Project Objectives

- **Solid Fundamentals:** Practice algorithms and data structures (the bread and butter of computing).
- **Logical Reasoning:** Develop the ability to break down complex problems into efficient solutions.
- **Technical Communication:** Learn to explain the reasoning behind the code, an essential skill in the AI era.
- **Collaboration:** Evolve together, reviewing solutions and sharing different approaches to the same problem.

---

## 📂 Folder Structure

To keep the repository organized and facilitate the search for specific solutions, we adopted a strict directory hierarchy. When adding your contribution, follow this model:

```text
challenges/
└── <platform-name>/            # leetcode, beecrowd, neetcode, others...
    └── <id>: <challenge-name>/ # Ex: "01: Two Sum" or "1001: Extremely Basic"
        └── <language>/         # python, cpp, java, typescript, etc.
            └── <solution-number>/ # 01, 02, 03... (for different methods/members)
                ├── solution.ext   # Source code file
                ├── README.md      # Logic explanation (optional)
                └── assets/        # Related images or prints (optional)
```

---

### Practical Example

If you solved the "Two Sum" challenge on LeetCode in Python and it's the group's first solution:
`challenges/leetcode/1: Two Sum/python/01/solution.py`

---

## 🤝 Organizers

This project was developed by the **Tutorial Education Program (PET)** - a program formed by a group of students from the Computer Engineering course at UFC Sobral.

### PET Interview Organization Team:

- [Cizé Lucas](https://github.com/CizeLucas)
- [Pâmela Maria](https://github.com/P4m3l4m4r14)
- [Vitória Emilly](https://github.com/vitsantos)

### Acknowledgments

- Initial idea that originated the group and Mentorship by [Henrique Vasconcelos](https://www.linkedin.com/in/henriquehsv/)
- PET Tutorship by [Prof. Dr. Wendley S. Silva](https://ec.ufc.br/pt/wendley/)
- Federal University of Ceará - Campus Sobral

---
