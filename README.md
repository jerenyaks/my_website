# KR Academy Website

Building tomorrow's legends through discipline, talent, and passion.

## Website Overview

A professional, responsive website for KR Academy football academy featuring:

- **Home Page** - Hero section with academy tagline, teams overview, and call-to-action
- **About Page** - Academy mission, coaching staff profiles (Calvin, Niky, Obaha, Griffins)
- **Teams Page** - Details on U15, U21, and Girls Team with focus areas
- **Schedule Page** - Weekly training schedule for all teams at Kitengela Railway
- **Gallery Page** - Photo/video showcase with Instagram links
- **Contact Page** - Contact form, phone numbers (+254 759 076880, +254 723 695749), location info
- **Enroll Page** - Full enrollment form with field validation

## Brand Identity

- **Primary Colour:** Deep Blue (#0052CC)
- **Secondary Colour:** Black (#000000)
- **Accent Colour:** Gold (#FFD700)
- **Logo/Crest:** KR Academy crest (see below)

## Files Structure

```
my_website/
├── index.html           (Home page)
├── about.html           (About & Coaches)
├── teams.html           (Teams info)
├── schedule.html        (Training schedule)
├── gallery.html         (Photo gallery)
├── contact.html         (Contact form)
├── enroll.html          (Enrollment form)
├── style.css            (Master stylesheet)
├── crest.png            (Academy crest - SEE INSTRUCTIONS BELOW)
└── README.md            (This file)
```

## Setup Instructions

### Step 1: Add the Academy Crest

The website references `crest.png` for the academy logo/crest. 

**ACTION REQUIRED:** 
- Save the KR Academy crest image as `crest.png` in the `my_website` folder
- The image file should be the PNG you provided with the blue and white design

Without this image, the navigation bar and hero sections will show a broken image icon.

### Step 2: Open in Browser

Open any of these files in your web browser:
- `index.html` for the home page
- Or navigate to the website folder and open `index.html`

### Step 3: Test All Features

- Navigation menu (should be sticky at top)
- All buttons and links
- Forms (Contact & Enrollment) - test submission
- Responsive design (resize browser or test on mobile)
- Brand colours throughout

## Features Implemented

✅ **Fully Responsive Design** - Works on desktop, tablet, mobile  
✅ **Professional Styling** - Brand colours, gradients, animations  
✅ **Navigation Bar** - Sticky header with active page highlighting  
✅ **Contact Information** - Phone numbers, location, Instagram  
✅ **Forms** - Contact and enrollment forms with validation  
✅ **Team Information** - U15, U21, Girls Team details  
✅ **Training Schedule** - Weekly schedule for all teams  
✅ **Coaching Staff** - Profile cards for all coaches  
✅ **Call-to-Action Buttons** - Enrollment prompts throughout  

## Customization Guide

### To Update Text Content:
- Edit any `.html` file with a text editor
- Look for the section you want to change
- Update the text between HTML tags
- Save and refresh browser

### To Update Colours:
- Open `style.css`
- Find the `:root` section at the top with colour variables:
  ```css
  --primary-blue: #0052CC;
  --dark-blue: #003399;
  --black: #000000;
  --white: #FFFFFF;
  --gold: #FFD700;
  ```
- Change hex codes as needed

### To Add Images:
- Save image files to the `my_website` folder
- Reference them in HTML: `<img src="image-name.png" alt="description">`

## Contact Information

**KR Academy**
- 📍 Kitengela Railway, Kenya
- 📞 +254 759 076880
- 📞 +254 723 695749
- 📱 Instagram: @kr_academyfc

**Tagline:** KR ndio nyumbani (KR is home)

## Coaching Staff

- **Coach Calvin** - Head Coach & Academy Director
- **Coach Niky** - Assistant Coach, Technical Training
- **Coach Obaha** - Defensive Specialist
- **Coach Griffins** - Fitness & Physical Development

## Next Steps

1. **Add Crest Image** - Save the PNG as `crest.png` in the website folder
2. **Test Website** - Open `index.html` in browser and test all pages/features
3. **Deploy** - Upload all files to a web hosting service (Netlify, Vercel, etc.)
4. **Domain** - Connect a custom domain (optional)
5. **Update Instagram Feed** - Link real Instagram posts to the Gallery page
6. **Contact Form Integration** - Set up email notifications for form submissions

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (iOS Safari, Chrome Mobile)

## Tips

- All pages use the same navigation and footer for consistency
- Forms are styled but backend submission needs server setup (optional)
- Images have placeholder emoji icons - replace with actual photos
- The site is mobile-responsive and will look good on all devices
- Theme colours are easy to customize in `style.css`

---

**Built for KR Academy** | Discipline • Talent • Passion 🔥⚽

For any website updates or modifications, contact the development team.
