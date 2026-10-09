"use client";

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
