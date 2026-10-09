"use client";

import { motion } from "framer-motion";
import { Mail, Download, Send } from "lucide-react";
import { FaGithub, FaLinkedin } from "react-icons/fa";

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
                  <FaGithub size={24} />
                </a>
                <a href="https://linkedin.com" target="_blank" rel="noreferrer" className="w-12 h-12 rounded-xl glass flex items-center justify-center text-white hover:bg-white/10 hover:text-blue-400 transition-all">
                  <FaLinkedin size={24} />
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
