"use client";

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
