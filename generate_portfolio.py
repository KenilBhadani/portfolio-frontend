import os
import json

# Ensure directories exist
base_dir = "src"
os.makedirs(os.path.join(base_dir, "components"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "app"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "lib"), exist_ok=True)

# 1. lib/utils.ts
with open(os.path.join(base_dir, "lib", "utils.ts"), "w", encoding="utf-8") as f:
    f.write("""import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
""")

# 2. globals.css
with open(os.path.join(base_dir, "app", "globals.css"), "w", encoding="utf-8") as f:
    f.write("""@import "tailwindcss";

@theme {
  --color-background: #060913;
  --color-foreground: #ffffff;
  --color-primary: #3b82f6;
  --color-primary-foreground: #ffffff;
  --color-accent: #8b5cf6;
  --color-card: rgba(17, 24, 39, 0.7);
  --color-card-border: rgba(55, 65, 81, 0.5);
  
  --font-sans: var(--font-inter), ui-sans-serif, system-ui, sans-serif;
  --font-mono: var(--font-fira-code), ui-monospace, SFMono-Regular, monospace;
}

:root {
  color-scheme: dark;
}

body {
  background-color: var(--color-background);
  color: var(--color-foreground);
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  scroll-behavior: smooth;
}

/* Glassmorphism utility */
.glass {
  background: var(--color-card);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid var(--color-card-border);
}

.text-gradient {
  background: linear-gradient(to right, #60a5fa, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hide-scrollbar::-webkit-scrollbar {
  display: none;
}
.hide-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
""")

# 3. layout.tsx
with open(os.path.join(base_dir, "app", "layout.tsx"), "w", encoding="utf-8") as f:
    f.write("""import type { Metadata } from "next";
import { Inter, Fira_Code } from "next/font/google";
import "./globals.css";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });
const firaCode = Fira_Code({ subsets: ["latin"], variable: "--font-fira-code" });

export const metadata: Metadata = {
  title: "Kenil Bhadani | AI/ML Engineer",
  description: "Portfolio of Kenil Bhadani, an AI/ML Engineer focused on Machine Learning, Deep Learning, Computer Vision, Data Science and Generative AI.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${inter.variable} ${firaCode.variable} dark`}>
      <body className="min-h-screen bg-background font-sans antialiased overflow-x-hidden selection:bg-primary/30 selection:text-white">
        {/* Subtle Background Effects */}
        <div className="fixed inset-0 z-[-1] bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-blue-900/20 via-background to-background"></div>
        <div className="fixed inset-0 z-[-1] bg-[radial-gradient(ellipse_at_bottom_left,_var(--tw-gradient-stops))] from-purple-900/20 via-background/0 to-background/0"></div>
        
        <Navbar />
        <main className="flex flex-col min-h-screen">
          {children}
        </main>
        <Footer />
      </body>
    </html>
  );
}
""")

# 4. page.tsx
with open(os.path.join(base_dir, "app", "page.tsx"), "w", encoding="utf-8") as f:
    f.write("""import Hero from "@/components/Hero";
import About from "@/components/About";
import Skills from "@/components/Skills";
import Projects from "@/components/Projects";
import Education from "@/components/Education";
import Certifications from "@/components/Certifications";
import Contact from "@/components/Contact";

export default function Home() {
  return (
    <>
      <Hero />
      <About />
      <Skills />
      <Projects />
      <Education />
      <Certifications />
      <Contact />
    </>
  );
}
""")

# 5. components/Navbar.tsx
with open(os.path.join(base_dir, "components", "Navbar.tsx"), "w", encoding="utf-8") as f:
    f.write(""""use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Menu, X, Github, Linkedin } from "lucide-react";
import Link from "next/link";

const navLinks = [
  { name: "Home", href: "#home" },
  { name: "About", href: "#about" },
  { name: "Skills", href: "#skills" },
  { name: "Projects", href: "#projects" },
  { name: "Education", href: "#education" },
  { name: "Certifications", href: "#certifications" },
  { name: "Contact", href: "#contact" },
];

export default function Navbar() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <header
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        isScrolled ? "glass shadow-lg shadow-black/20 py-4" : "bg-transparent py-6"
      }`}
    >
      <div className="container mx-auto px-6 md:px-12 flex items-center justify-between">
        <Link href="#home" className="text-xl font-bold font-mono tracking-tighter">
          KB<span className="text-primary">.</span>
        </Link>

        {/* Desktop Nav */}
        <nav className="hidden md:flex items-center gap-8">
          <ul className="flex items-center gap-6">
            {navLinks.map((link) => (
              <li key={link.name}>
                <Link
                  href={link.href}
                  className="text-sm text-gray-300 hover:text-white transition-colors duration-200"
                >
                  {link.name}
                </Link>
              </li>
            ))}
          </ul>
          <div className="flex items-center gap-4 border-l border-gray-700 pl-6">
            <a href="https://github.com" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-white transition-colors">
              <Github size={20} />
            </a>
            <a href="https://linkedin.com" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-white transition-colors">
              <Linkedin size={20} />
            </a>
          </div>
        </nav>

        {/* Mobile Nav Toggle */}
        <button
          className="md:hidden text-gray-300 hover:text-white"
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
        >
          {mobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
        </button>
      </div>

      {/* Mobile Nav Menu */}
      <AnimatePresence>
        {mobileMenuOpen && (
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="absolute top-full left-0 right-0 glass border-t-0 p-6 md:hidden flex flex-col gap-4 shadow-xl"
          >
            <ul className="flex flex-col gap-4">
              {navLinks.map((link) => (
                <li key={link.name}>
                  <Link
                    href={link.href}
                    onClick={() => setMobileMenuOpen(false)}
                    className="block text-base text-gray-300 hover:text-white transition-colors duration-200"
                  >
                    {link.name}
                  </Link>
                </li>
              ))}
            </ul>
            <div className="flex items-center gap-4 pt-4 border-t border-gray-700">
              <a href="https://github.com" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-white">
                <Github size={24} />
              </a>
              <a href="https://linkedin.com" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-white">
                <Linkedin size={24} />
              </a>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}
""")

# 6. components/Hero.tsx
with open(os.path.join(base_dir, "components", "Hero.tsx"), "w", encoding="utf-8") as f:
    f.write(""""use client";

import { motion } from "framer-motion";
import { ArrowRight, Download, Terminal, Network, Code2, Database } from "lucide-react";
import Link from "next/link";

export default function Hero() {
  return (
    <section id="home" className="relative min-h-screen flex items-center justify-center pt-24 overflow-hidden">
      <div className="container mx-auto px-6 md:px-12 grid lg:grid-cols-2 gap-12 items-center">
        
        <motion.div 
          initial={{ opacity: 0, x: -50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
          className="flex flex-col gap-6 relative z-10"
        >
          <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-sm font-medium w-fit">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
            </span>
            Available for AI/ML Opportunities
          </div>
          
          <h1 className="text-5xl md:text-6xl lg:text-7xl font-extrabold tracking-tight">
            Hi, I'm <span className="text-white">Kenil Bhadani</span>
          </h1>
          
          <h2 className="text-2xl md:text-3xl font-semibold text-gray-300 leading-tight">
            AI/ML Engineer building intelligent solutions with <span className="text-gradient">Machine Learning, Deep Learning & Generative AI.</span>
          </h2>
          
          <p className="text-gray-400 text-lg max-w-xl leading-relaxed">
            I build practical AI and machine learning applications using Python, Scikit-learn, TensorFlow, Computer Vision and modern Generative AI technologies.
          </p>
          
          <div className="flex flex-wrap items-center gap-4 mt-4">
            <Link 
              href="#projects" 
              className="px-6 py-3 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-medium flex items-center gap-2 transition-all hover:scale-105 active:scale-95 shadow-[0_0_20px_rgba(37,99,235,0.3)]"
            >
              View Projects <ArrowRight size={18} />
            </Link>
            
            <a 
              href="/resume.pdf" 
              className="px-6 py-3 rounded-xl glass hover:bg-white/10 text-white font-medium flex items-center gap-2 transition-all hover:scale-105 active:scale-95"
            >
              <Download size={18} /> Download Resume
            </a>
          </div>
        </motion.div>

        {/* Right side abstract visual */}
        <motion.div
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1, delay: 0.2 }}
          className="relative hidden lg:flex justify-center items-center h-[500px]"
        >
          {/* Abstract glowing sphere */}
          <div className="absolute w-[400px] h-[400px] bg-blue-600/20 rounded-full blur-[80px] animate-pulse"></div>
          
          {/* Decorative floating elements */}
          <motion.div 
            animate={{ y: [-10, 10, -10], rotate: [0, 5, 0] }}
            transition={{ repeat: Infinity, duration: 5, ease: "easeInOut" }}
            className="absolute top-10 right-20 glass p-4 rounded-2xl border border-white/10"
          >
            <Network className="text-blue-400 w-8 h-8" />
          </motion.div>
          
          <motion.div 
            animate={{ y: [10, -10, 10], rotate: [0, -5, 0] }}
            transition={{ repeat: Infinity, duration: 4, ease: "easeInOut", delay: 1 }}
            className="absolute bottom-20 left-10 glass p-4 rounded-2xl border border-white/10"
          >
            <Database className="text-purple-400 w-8 h-8" />
          </motion.div>

          <motion.div 
            animate={{ y: [-15, 15, -15], rotate: [0, 10, 0] }}
            transition={{ repeat: Infinity, duration: 6, ease: "easeInOut", delay: 2 }}
            className="absolute top-40 left-0 glass p-4 rounded-2xl border border-white/10"
          >
            <Code2 className="text-emerald-400 w-8 h-8" />
          </motion.div>

          {/* Center piece */}
          <div className="relative glass w-64 h-64 rounded-full flex items-center justify-center border border-blue-500/30 shadow-[0_0_40px_rgba(59,130,246,0.2)]">
            <div className="absolute inset-2 border border-purple-500/30 rounded-full animate-[spin_10s_linear_infinite]"></div>
            <div className="absolute inset-6 border border-blue-400/20 rounded-full animate-[spin_15s_linear_infinite_reverse]"></div>
            <Terminal className="w-16 h-16 text-white/80" />
          </div>
        </motion.div>

      </div>
    </section>
  );
}
""")

# 7. components/About.tsx
with open(os.path.join(base_dir, "components", "About.tsx"), "w", encoding="utf-8") as f:
    f.write(""""use client";

import { motion } from "framer-motion";
import { GraduationCap, BrainCircuit, Code, Braces } from "lucide-react";

export default function About() {
  const stats = [
    { icon: GraduationCap, label: "BCA Graduate", desc: "Computer Science" },
    { icon: BrainCircuit, label: "AI/ML Focused", desc: "Core Specialization" },
    { icon: Code, label: "Python Developer", desc: "Primary Ecosystem" },
    { icon: Braces, label: "Project-Based Learning", desc: "Hands-on Experience" },
  ];

  return (
    <section id="about" className="py-24 relative">
      <div className="container mx-auto px-6 md:px-12">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-12"
        >
          <h2 className="text-3xl md:text-4xl font-bold mb-4">About Me</h2>
          <div className="w-20 h-1 bg-blue-600 rounded-full"></div>
        </motion.div>

        <div className="grid lg:grid-cols-2 gap-12 items-center">
          <motion.div 
            initial={{ opacity: 0, x: -30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            className="space-y-6 text-gray-300 text-lg"
          >
            <p>
              I am a BCA graduate highly focused on <strong className="text-white">Artificial Intelligence and Machine Learning</strong>. My passion lies in understanding how data can be transformed into intelligent, predictive solutions.
            </p>
            <p>
              My hands-on learning journey spans across <strong className="text-blue-400">Machine Learning, Deep Learning, Computer Vision, Data Science, and Generative AI</strong>. I believe in learning by doing, which is why my focus is heavily oriented towards practical project development—from initial data exploration and model building, all the way to evaluation and deployment.
            </p>
            <p>
              As an entry-level engineer, I am eager to apply my technical foundations in real-world scenarios, contribute to impactful AI products, and continuously grow my expertise in modern AI stacks.
            </p>
          </motion.div>

          <motion.div 
            initial={{ opacity: 0, x: 30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            className="grid grid-cols-2 gap-4"
          >
            {stats.map((stat, idx) => (
              <div key={idx} className="glass p-6 rounded-2xl flex flex-col items-center text-center gap-3 hover:border-blue-500/50 transition-colors">
                <div className="w-12 h-12 rounded-full bg-blue-500/10 flex items-center justify-center text-blue-400">
                  <stat.icon size={24} />
                </div>
                <div>
                  <h3 className="text-white font-semibold">{stat.label}</h3>
                  <p className="text-sm text-gray-400">{stat.desc}</p>
                </div>
              </div>
            ))}
          </motion.div>
        </div>
      </div>
    </section>
  );
}
""")

# 8. components/Skills.tsx
with open(os.path.join(base_dir, "components", "Skills.tsx"), "w", encoding="utf-8") as f:
    f.write(""""use client";

import { motion } from "framer-motion";
import { Brain, Cpu, Sparkles, Rocket } from "lucide-react";

const skillCategories = [
  {
    title: "Machine Learning",
    icon: Brain,
    color: "text-blue-400",
    bgColor: "bg-blue-400/10",
    skills: ["Python", "NumPy", "Pandas", "Scikit-learn", "Matplotlib", "Seaborn", "Feature Engineering", "Model Evaluation"]
  },
  {
    title: "Deep Learning",
    icon: Cpu,
    color: "text-purple-400",
    bgColor: "bg-purple-400/10",
    skills: ["TensorFlow", "Keras", "Neural Networks", "CNN", "Transfer Learning", "Computer Vision"]
  },
  {
    title: "Generative AI",
    icon: Sparkles,
    color: "text-emerald-400",
    bgColor: "bg-emerald-400/10",
    skills: ["LLMs", "Prompt Engineering", "RAG", "Transformers", "LangChain"]
  },
  {
    title: "Development & Deployment",
    icon: Rocket,
    color: "text-orange-400",
    bgColor: "bg-orange-400/10",
    skills: ["Git", "GitHub", "Streamlit", "Flask/FastAPI", "REST APIs", "Docker", "Vercel"]
  }
];

export default function Skills() {
  return (
    <section id="skills" className="py-24 relative bg-black/20">
      <div className="container mx-auto px-6 md:px-12">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-12"
        >
          <h2 className="text-3xl md:text-4xl font-bold mb-4">Technical Skills</h2>
          <div className="w-20 h-1 bg-blue-600 rounded-full"></div>
        </motion.div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {skillCategories.map((category, idx) => (
            <motion.div
              key={idx}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: idx * 0.1 }}
              className="glass p-6 rounded-2xl hover:-translate-y-2 transition-transform duration-300"
            >
              <div className={`w-12 h-12 rounded-xl flex items-center justify-center mb-6 ${category.bgColor} ${category.color}`}>
                <category.icon size={24} />
              </div>
              <h3 className="text-xl font-bold text-white mb-4">{category.title}</h3>
              <div className="flex flex-wrap gap-2">
                {category.skills.map((skill, sIdx) => (
                  <span 
                    key={sIdx}
                    className="px-3 py-1 bg-white/5 border border-white/10 rounded-full text-sm text-gray-300 font-medium"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
""")

# 9. components/Projects.tsx
with open(os.path.join(base_dir, "components", "Projects.tsx"), "w", encoding="utf-8") as f:
    f.write(""""use client";

import { motion } from "framer-motion";
import { Github, ExternalLink, Activity } from "lucide-react";

const projects = [
  {
    title: "Phishing URL Detection",
    description: "A machine learning system that detects whether a URL is phishing or legitimate using URL-based features.",
    problem: "Identifying malicious links before users click them by analyzing structural URL attributes.",
    tech: ["Python", "Pandas", "Scikit-learn", "Random Forest"],
    metrics: [
      { label: "Accuracy", value: "99.80%" },
      { label: "Precision", value: "99.70%" },
      { label: "Recall", value: "99.95%" },
      { label: "F1 Score", value: "99.82%" },
    ],
    github: "https://github.com",
    demo: null,
    gradient: "from-blue-600/20 to-cyan-600/20"
  },
  {
    title: "Computer Vision Image Classification",
    description: "Deep learning model utilizing transfer learning to accurately classify images across distinct categories.",
    problem: "Building a highly accurate image classifier without training massive models from scratch.",
    tech: ["TensorFlow", "Keras", "CNN", "Transfer Learning"],
    metrics: [
      { label: "Validation Acc", value: "High" },
      { label: "Loss", value: "Minimized" },
    ],
    github: "https://github.com",
    demo: null,
    gradient: "from-purple-600/20 to-pink-600/20"
  },
  {
    title: "Home Loan Default Prediction",
    description: "Predictive model to analyze customer data and determine loan default eligibility.",
    problem: "Assessing financial risk efficiently to automate loan approval processes.",
    tech: ["Python", "Pandas", "Scikit-learn", "Machine Learning"],
    metrics: [
      { label: "Predictive Power", value: "Robust" },
      { label: "Feature Impt", value: "Extracted" },
    ],
    github: "https://github.com",
    demo: null,
    gradient: "from-emerald-600/20 to-teal-600/20"
  },
  {
    title: "Generative AI / RAG Pipeline",
    description: "Advanced Retrieval-Augmented Generation system for document Q&A.",
    problem: "Answering complex queries reliably based on custom context.",
    tech: ["LLMs", "LangChain", "Vector DB", "Transformers"],
    metrics: [],
    github: null,
    demo: null,
    comingSoon: true,
    gradient: "from-orange-600/20 to-red-600/20"
  }
];

export default function Projects() {
  return (
    <section id="projects" className="py-24 relative">
      <div className="container mx-auto px-6 md:px-12">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-12 flex flex-col md:flex-row md:items-end justify-between gap-4"
        >
          <div>
            <h2 className="text-3xl md:text-4xl font-bold mb-4">Featured Projects</h2>
            <div className="w-20 h-1 bg-blue-600 rounded-full mb-4"></div>
            <p className="text-gray-400 max-w-2xl text-lg">Practical applications of AI/ML showcasing end-to-end development, from data processing to model evaluation.</p>
          </div>
        </motion.div>

        <div className="grid md:grid-cols-2 gap-8">
          {projects.map((project, idx) => (
            <motion.div
              key={idx}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: idx * 0.1 }}
              className={`glass rounded-2xl overflow-hidden group hover:border-blue-500/30 transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_10px_30px_rgba(59,130,246,0.1)] relative`}
            >
              {/* Background abstract gradient */}
              <div className={`absolute inset-0 bg-gradient-to-br ${project.gradient} opacity-0 group-hover:opacity-100 transition-opacity duration-500`}></div>
              
              <div className="p-8 relative z-10 flex flex-col h-full">
                {project.comingSoon && (
                  <span className="absolute top-6 right-6 px-3 py-1 bg-white/10 rounded-full text-xs font-semibold text-white uppercase tracking-wider backdrop-blur-md border border-white/10">
                    Coming Soon
                  </span>
                )}
                
                <h3 className="text-2xl font-bold text-white mb-3 group-hover:text-blue-400 transition-colors">{project.title}</h3>
                <p className="text-gray-400 mb-4">{project.description}</p>
                
                <div className="mb-6">
                  <p className="text-sm text-gray-500 font-medium mb-1 uppercase tracking-wider">Problem Solved</p>
                  <p className="text-gray-300 text-sm">{project.problem}</p>
                </div>

                {/* Metrics */}
                {project.metrics.length > 0 && (
                  <div className="mb-6 bg-black/30 rounded-xl p-4 border border-white/5">
                    <div className="flex items-center gap-2 mb-3 text-sm font-medium text-gray-400">
                      <Activity size={16} /> Key Metrics
                    </div>
                    <div className="grid grid-cols-2 gap-3">
                      {project.metrics.map((metric, mIdx) => (
                        <div key={mIdx}>
                          <p className="text-xs text-gray-500">{metric.label}</p>
                          <p className="text-white font-mono font-semibold">{metric.value}</p>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                <div className="mt-auto pt-6 flex flex-wrap items-center justify-between gap-4 border-t border-white/10">
                  <div className="flex flex-wrap gap-2">
                    {project.tech.map((t, tIdx) => (
                      <span key={tIdx} className="text-xs font-medium text-blue-300 bg-blue-500/10 px-2 py-1 rounded">
                        {t}
                      </span>
                    ))}
                  </div>
                  
                  <div className="flex items-center gap-3">
                    {project.github && (
                      <a href={project.github} target="_blank" rel="noreferrer" className="p-2 rounded-full bg-white/5 hover:bg-white/20 text-white transition-colors">
                        <Github size={20} />
                      </a>
                    )}
                    {project.demo && (
                      <a href={project.demo} target="_blank" rel="noreferrer" className="p-2 rounded-full bg-blue-600 hover:bg-blue-500 text-white transition-colors">
                        <ExternalLink size={20} />
                      </a>
                    )}
                  </div>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
""")

# 10. components/Education.tsx
with open(os.path.join(base_dir, "components", "Education.tsx"), "w", encoding="utf-8") as f:
    f.write(""""use client";

import { motion } from "framer-motion";
import { BookOpen, ChevronDown } from "lucide-react";

export default function Education() {
  const journey = [
    "Data Science",
    "Machine Learning",
    "Deep Learning",
    "Computer Vision",
    "Generative AI"
  ];

  return (
    <section id="education" className="py-24 relative bg-black/20">
      <div className="container mx-auto px-6 md:px-12">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-12 flex flex-col items-center text-center"
        >
          <h2 className="text-3xl md:text-4xl font-bold mb-4">Education & Learning Journey</h2>
          <div className="w-20 h-1 bg-blue-600 rounded-full mb-8"></div>
        </motion.div>

        <div className="grid md:grid-cols-2 gap-12 items-start max-w-5xl mx-auto">
          {/* Formal Education */}
          <motion.div
            initial={{ opacity: 0, x: -30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            className="glass p-8 rounded-2xl relative overflow-hidden"
          >
            <div className="absolute top-0 right-0 w-32 h-32 bg-blue-500/10 rounded-bl-full"></div>
            
            <div className="flex items-center gap-4 mb-6 relative z-10">
              <div className="w-12 h-12 bg-blue-600 rounded-xl flex items-center justify-center text-white shadow-lg shadow-blue-600/30">
                <BookOpen size={24} />
              </div>
              <div>
                <h3 className="text-2xl font-bold text-white">Bachelor of Computer Applications</h3>
                <p className="text-blue-400 font-medium">BCA Graduate</p>
              </div>
            </div>
            
            <p className="text-gray-400 leading-relaxed relative z-10">
              Completed foundational education in computer science, software engineering, and database management, providing a strong structural backing for complex AI/ML algorithms and production deployments.
            </p>
          </motion.div>

          {/* Learning Progression */}
          <motion.div
            initial={{ opacity: 0, x: 30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            className="flex flex-col gap-4"
          >
            <h3 className="text-xl font-semibold text-white mb-2 px-2">Technical Progression</h3>
            
            {journey.map((step, idx) => (
              <div key={idx} className="flex flex-col">
                <motion.div 
                  initial={{ opacity: 0, y: 10 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ delay: idx * 0.15 }}
                  className="glass p-4 rounded-xl border border-white/5 flex items-center justify-between group hover:border-blue-500/30 transition-colors"
                >
                  <span className="text-gray-300 font-medium group-hover:text-white transition-colors">{step}</span>
                  <div className="w-8 h-8 rounded-full bg-white/5 flex items-center justify-center text-blue-400 font-mono text-xs">
                    0{idx + 1}
                  </div>
                </motion.div>
                {idx < journey.length - 1 && (
                  <div className="h-6 w-full flex justify-center py-1">
                    <ChevronDown size={16} className="text-gray-600" />
                  </div>
                )}
              </div>
            ))}
          </motion.div>
        </div>
      </div>
    </section>
  );
}
""")

# 11. components/Certifications.tsx
with open(os.path.join(base_dir, "components", "Certifications.tsx"), "w", encoding="utf-8") as f:
    f.write(""""use client";

import { motion } from "framer-motion";
import { Award, ExternalLink } from "lucide-react";

export default function Certifications() {
  const certifications = [
    {
      title: "Certified AI & ML Specialist",
      org: "DataMites",
      year: "Completed",
      link: "#"
    }
  ];

  return (
    <section id="certifications" className="py-24 relative">
      <div className="container mx-auto px-6 md:px-12 max-w-5xl">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-12"
        >
          <h2 className="text-3xl md:text-4xl font-bold mb-4">Certifications</h2>
          <div className="w-20 h-1 bg-blue-600 rounded-full"></div>
        </motion.div>

        <div className="grid md:grid-cols-2 gap-6">
          {certifications.map((cert, idx) => (
            <motion.div
              key={idx}
              initial={{ opacity: 0, scale: 0.95 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              className="glass p-6 rounded-2xl border-l-4 border-l-blue-500 flex items-start gap-4 hover:bg-white/5 transition-colors"
            >
              <div className="w-10 h-10 rounded-full bg-blue-500/20 flex items-center justify-center text-blue-400 shrink-0 mt-1">
                <Award size={20} />
              </div>
              <div className="flex-1">
                <h3 className="text-lg font-bold text-white mb-1">{cert.title}</h3>
                <p className="text-blue-300 text-sm font-medium mb-2">{cert.org}</p>
                <div className="flex items-center justify-between mt-4 pt-4 border-t border-white/10">
                  <span className="text-gray-400 text-sm">{cert.year}</span>
                  {cert.link !== "#" && (
                    <a href={cert.link} className="text-gray-400 hover:text-white flex items-center gap-1 text-sm transition-colors">
                      Credential <ExternalLink size={14} />
                    </a>
                  )}
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
""")

# 12. components/Contact.tsx
with open(os.path.join(base_dir, "components", "Contact.tsx"), "w", encoding="utf-8") as f:
    f.write(""""use client";

import { motion } from "framer-motion";
import { Mail, Github, Linkedin, Download, Send } from "lucide-react";

export default function Contact() {
  return (
    <section id="contact" className="py-24 relative bg-black/20">
      <div className="container mx-auto px-6 md:px-12 max-w-6xl">
        
        {/* Strong CTA Banner */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="glass rounded-3xl p-8 md:p-12 mb-20 bg-gradient-to-br from-blue-900/40 to-purple-900/40 border border-blue-500/30 text-center md:text-left flex flex-col md:flex-row items-center justify-between gap-8"
        >
          <div>
            <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">Want to know more about my work?</h2>
            <p className="text-blue-200 text-lg max-w-2xl">Download my resume to explore my skills, projects and AI/ML journey in detail.</p>
          </div>
          <a 
            href="/resume.pdf" 
            className="px-8 py-4 rounded-xl bg-white text-black font-bold flex items-center gap-2 hover:scale-105 transition-transform shrink-0"
          >
            <Download size={20} /> Download Resume
          </a>
        </motion.div>

        <div className="grid md:grid-cols-2 gap-12">
          {/* Contact Info */}
          <motion.div
            initial={{ opacity: 0, x: -30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">Let's Build Something Intelligent</h2>
            <p className="text-gray-400 text-lg mb-8">
              I'm open to AI/ML opportunities, collaborations and interesting projects. Feel free to reach out.
            </p>

            <div className="flex flex-col gap-6">
              <a href="mailto:kenilbhadani@example.com" className="flex items-center gap-4 glass p-4 rounded-xl hover:border-blue-500/50 transition-colors w-fit pr-8">
                <div className="w-12 h-12 rounded-full bg-blue-500/20 flex items-center justify-center text-blue-400">
                  <Mail size={20} />
                </div>
                <div>
                  <p className="text-sm text-gray-400">Email Me</p>
                  <p className="text-white font-medium">kenilbhadani@example.com</p>
                </div>
              </a>
              
              <div className="flex gap-4">
                <a href="https://github.com" target="_blank" rel="noreferrer" className="w-12 h-12 rounded-xl glass flex items-center justify-center text-white hover:bg-white/10 hover:text-blue-400 transition-all">
                  <Github size={24} />
                </a>
                <a href="https://linkedin.com" target="_blank" rel="noreferrer" className="w-12 h-12 rounded-xl glass flex items-center justify-center text-white hover:bg-white/10 hover:text-blue-400 transition-all">
                  <Linkedin size={24} />
                </a>
              </div>
            </div>
          </motion.div>

          {/* Contact Form */}
          <motion.div
            initial={{ opacity: 0, x: 30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            className="glass p-8 rounded-2xl"
          >
            <form action="mailto:kenilbhadani@example.com" method="GET" encType="text/plain" className="flex flex-col gap-6">
              <div>
                <label className="block text-sm font-medium text-gray-400 mb-2">Name</label>
                <input 
                  type="text" 
                  className="w-full bg-black/50 border border-white/10 rounded-xl p-4 text-white focus:outline-none focus:border-blue-500 transition-colors"
                  placeholder="John Doe"
                  required
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-400 mb-2">Email</label>
                <input 
                  type="email" 
                  className="w-full bg-black/50 border border-white/10 rounded-xl p-4 text-white focus:outline-none focus:border-blue-500 transition-colors"
                  placeholder="john@example.com"
                  required
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-400 mb-2">Message</label>
                <textarea 
                  rows={4}
                  className="w-full bg-black/50 border border-white/10 rounded-xl p-4 text-white focus:outline-none focus:border-blue-500 transition-colors resize-none"
                  placeholder="Let's talk about AI..."
                  required
                ></textarea>
              </div>
              <button 
                type="submit"
                className="w-full py-4 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-bold flex items-center justify-center gap-2 transition-colors"
              >
                Send Message <Send size={18} />
              </button>
            </form>
          </motion.div>
        </div>
      </div>
    </section>
  );
}
""")

# 13. components/Footer.tsx
with open(os.path.join(base_dir, "components", "Footer.tsx"), "w", encoding="utf-8") as f:
    f.write(""""use client";

import { ArrowUp } from "lucide-react";

export default function Footer() {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <footer className="py-8 border-t border-white/10 bg-black/50 relative">
      <div className="container mx-auto px-6 md:px-12 flex flex-col md:flex-row items-center justify-between gap-4">
        
        <div>
          <p className="text-white font-semibold">© 2026 Kenil Bhadani</p>
          <p className="text-sm text-gray-500">AI/ML Engineer</p>
        </div>

        <div className="flex items-center gap-6 text-sm text-gray-400">
          <a href="https://github.com" className="hover:text-white transition-colors">GitHub</a>
          <a href="https://linkedin.com" className="hover:text-white transition-colors">LinkedIn</a>
          <a href="mailto:kenilbhadani@example.com" className="hover:text-white transition-colors">Email</a>
        </div>

        <button 
          onClick={scrollToTop}
          className="w-10 h-10 rounded-full glass flex items-center justify-center text-gray-400 hover:text-white hover:bg-white/10 transition-colors"
          aria-label="Back to top"
        >
          <ArrowUp size={20} />
        </button>

      </div>
    </footer>
  );
}
""")

print("Successfully generated all Next.js TSX files.")
