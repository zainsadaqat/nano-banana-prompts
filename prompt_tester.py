#!/usr/bin/env python3
"""
Nano Banana Prompt Tester
A simple script to help you test and organize your favorite prompts.
"""

import os
import json
from datetime import datetime

class PromptTester:
    def __init__(self):
        self.favorites_file = "my_favorite_prompts.json"
        self.load_favorites()
    
    def load_favorites(self):
        """Load saved favorite prompts"""
        if os.path.exists(self.favorites_file):
            with open(self.favorites_file, 'r') as f:
                self.favorites = json.load(f)
        else:
            self.favorites = []
    
    def save_favorites(self):
        """Save favorite prompts to file"""
        with open(self.favorites_file, 'w') as f:
            json.dump(self.favorites, f, indent=2)
    
    def add_favorite(self, title, prompt, category="General"):
        """Add a prompt to favorites"""
        favorite = {
            "title": title,
            "prompt": prompt,
            "category": category,
            "added_date": datetime.now().isoformat(),
            "use_count": 0
        }
        self.favorites.append(favorite)
        self.save_favorites()
        print(f"✅ Added '{title}' to favorites!")
    
    def list_favorites(self):
        """List all favorite prompts"""
        if not self.favorites:
            print("📝 No favorite prompts yet. Use add_favorite() to add some!")
            return
        
        print("\n🍌 Your Favorite Nano Banana Prompts:")
        print("=" * 50)
        
        for i, fav in enumerate(self.favorites, 1):
            print(f"\n{i}. {fav['title']} ({fav['category']})")
            print(f"   Used {fav['use_count']} times")
            print(f"   Prompt: {fav['prompt']}")
    
    def use_prompt(self, index):
        """Mark a prompt as used and copy to clipboard if possible"""
        if 0 <= index < len(self.favorites):
            self.favorites[index]['use_count'] += 1
            self.save_favorites()
            
            prompt = self.favorites[index]['prompt']
            print(f"📋 Prompt ready to use:")
            print(f"   {prompt}")
            print(f"\n💡 Remember to replace [PLACEHOLDERS] with your specific content!")
            
            # Try to copy to clipboard
            try:
                import pyperclip
                pyperclip.copy(prompt)
                print("✅ Copied to clipboard!")
            except ImportError:
                print("💡 Install 'pyperclip' to auto-copy prompts to clipboard")
        else:
            print("❌ Invalid prompt number")

# Example usage and pre-loaded favorites
if __name__ == "__main__":
    tester = PromptTester()
    
    # Add some popular prompts as examples
    if not tester.favorites:
        print("🚀 Setting up with popular Nano Banana prompts...")
        
        tester.add_favorite(
            "Email Shortener",
            "Rewrite this email to be 50% shorter while maintaining all key information and a professional tone: [YOUR EMAIL TEXT]",
            "Business"
        )
        
        tester.add_favorite(
            "Simple Explainer", 
            "Explain [COMPLEX CONCEPT] using only common words a 12-year-old would know, then give a real-world analogy.",
            "Learning"
        )
        
        tester.add_favorite(
            "Debug Helper",
            "I'm getting [ERROR MESSAGE]. Give me a 3-step debugging strategy starting with the most likely cause.",
            "Technical"
        )
        
        tester.add_favorite(
            "Story Starter",
            "Write a compelling opening sentence for a story that combines [GENRE] with an unexpected element. Make it grab attention immediately.",
            "Creative"
        )
    
    # Show available prompts
    tester.list_favorites()
    
    print("\n" + "=" * 50)
    print("🛠️  How to use this script:")
    print("   tester.add_favorite('Title', 'Prompt text', 'Category')")
    print("   tester.list_favorites()")
    print("   tester.use_prompt(0)  # Use first prompt")
    print("=" * 50)