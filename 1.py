# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import scrolledtext, font, messagebox, Menu
from textblob import TextBlob
import datetime
import json
import re
import random
import webbrowser

# --- Language Content Data ---
# Enhanced with 3 new languages: Bengali, Tamil, and Marathi
LANG_DATA = {
    'en': {
        'title': "Digital Literacy Chatbot",
        'lang_select_prompt': "Please select a language for the chatbot:",
        'lang_desc': "English",
        'welcome': "Hello! I am your Digital Literacy Chatbot, created by Group 7. I can help you learn about online safety and skills. Type 'help' to see all available commands.",
        'info_intro': "🌐 What is Digital Literacy?",
        'info_content': "Digital literacy is the ability to use digital devices like computers, mobile phones, and the internet correctly. It helps us in online services, banking, education, and communication.\n\nExamples:\n - Using online banking\n - Sending emails\n - Creating strong passwords\n - Following cybersecurity rules",
        'security_tips': "🔒 Online Security Tips",
        'security_content': "Cybersecurity is key for online safety.\n1. **OTP Warning**: Never share your One-Time Password (OTP) with anyone, not even bank employees. An OTP is for your use only.\n2. **Phishing**: Be cautious of suspicious emails or messages asking for personal information.\n3. **Strong Passwords**: Use a mix of letters, numbers, and special characters.\n4. **Public Wi-Fi**: Avoid sensitive transactions (like banking) on public Wi-Fi networks.",
        'quiz_intro': "📝 Let's do a quick quiz:\n",
        'q1': "1️⃣ Question: What should a strong password include?",
        'q1_options': "a) Only names\nb) A mix of letters, numbers, and special characters\nc) Date of birth",
        'q1_ans': 'b',
        'q2': "2️⃣ Question: What should you do with a link sent by an unknown person?",
        'q2_options': "a) Click on it immediately\nb) Ignore it\nc) Share it with everyone",
        'q2_ans': 'b',
        'q3': "3️⃣ Question: Should you share your OTP with a bank representative?",
        'q3_options': "a) Yes\nb) No, never\nc) Only if they call you from a bank number",
        'q3_ans': 'b',
        'q4': "4️⃣ Question: What is phishing?",
        'q4_options': "a) Fishing in a pond\nb) Trying to steal personal information using fake emails\nc) A type of online game",
        'q4_ans': 'b',
        'q5': "5️⃣ Question: Is it safe to do online banking on public Wi-Fi?",
        'q5_options': "a) Yes\nb) No, it's risky\nc) Only if the Wi-Fi is free",
        'q5_ans': 'b',
        'correct': "Correct! ✅",
        'incorrect': "Incorrect. ❌ The correct answer is: ",
        'your_score': "🎉 Your final score: ",
        'quiz_end_excellent': "Great job! You're a digital literacy expert.",
        'quiz_end_good': "You're on the right track! A little more practice will make you an expert.",
        'quiz_end_average': "Keep learning! Practice makes perfect.",
        'nlp_positive': "Your feedback is much appreciated! Thanks for the positive words. 😊",
        'nlp_negative': "I'm sorry to hear that. How can I improve to better assist you? 🤔",
        'nlp_neutral': "Okay, I understand. If you have any questions, feel free to ask. 🧐",
        'unknown_command': "I'm sorry, I don't understand that. Type 'help' to see the list of available commands.",
        'otp_warning': "🚫 SECURITY ALERT: It looks like you mentioned an OTP. Remember, never share your One-Time Password with anyone, even if they claim to be from a bank or any other service. Stay safe online!",
        'time': "The current time is: ",
        'date': "Today's date is: ",
        'weather': "Current weather in Lucknow: {weather_desc}",
        'image_prompt': "Please describe the image you want me to generate.",
        'image_generating': "🎨 Generating your image: '{prompt}'. This may take a moment...",
        'image_link': "🖼️ Your image is ready! View it here: ",
        'joke_intro': "😂 Here's a joke for you:",
        'jokes': [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why was the computer cold? Because it left its Windows open!",
            "I'm on a seafood diet. I see food, and I eat it.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ],
        'agri_intro': "🌾 Agriculture and Government Schemes",
        'agri_content': "Agriculture is the science and practice of cultivating plants and livestock. Here are some key Government schemes that help farmers:\n\n - **Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)**: An income support scheme for farmers.\n Link: https://pmkisan.gov.in/\n\n - **Pradhan Mantri Fasal Bima Yojana (PMFBY)**: A crop insurance scheme to protect farmers from losses.\n Link: https://pmfby.gov.in/\n\n - **Kisan Credit Card (KCC)**: A scheme to provide timely credit to farmers.\n Link: https://www.india.gov.in/schemes-kisan-credit-card-scheme\n\n - **Pradhan Mantri Krishi Sinchai Yojana (PMKSY)**: Aims to provide assured irrigation to every farm in the country.\n Link: https://pmksy.gov.in/\n\n - **GOBARdhan Scheme**: A 'Waste to Wealth' initiative for rural areas to convert solid waste and cattle dung into useful resources like biogas and organic manure.\n Link: https://sbm.gov.in/gbdhn/index",
        'health_intro': "🏥 Health Consultation and Schemes",
        'health_content': "Here's how you can get health consultations and information about government health schemes:\n\n - **eSanjeevani**: A national telemedicine service by the Government of India that offers free online doctor consultations.\n Link: https://esanjeevani.mohfw.gov.in/\n\n - **Ayushman Bharat - Pradhan Mantri Jan Arogya Yojana (PM-JAY)**: The world's largest health assurance scheme providing a health cover of ₹5 lakh per family per year for poor and vulnerable families.\n Link: https://nha.gov.in/PM-JAY",
        'sanitation_intro': "🚽 Sanitation Awareness",
        'sanitation_content': "Sanitation awareness is crucial for community health. The Government of India has launched a massive campaign to promote hygiene and cleanliness.\n\n - **Swachh Bharat Mission (SBM)**: A nationwide campaign to eliminate open defecation and improve solid waste management. It provides financial assistance for building toilets in both rural and urban areas.\n Link: https://swachhbharatmission.gov.in/\n\n - **Role of National Health Mission (NHM)**: NHM focuses on improving health outcomes, which are directly linked to sanitation and hygiene. It works to create awareness about healthy sanitation practices to prevent diseases.",
        'skills_intro': "🎓 Skills and Education",
        'skills_content': "Skill development and education are essential for individual growth and national progress. Here are key government initiatives:\n\n - **Pradhan Mantri Kaushal Vikas Yojana (PMKVY)**: The flagship scheme to enable a large number of Indian youth to take up industry-relevant skill training to secure a better livelihood.\n Link: https://pmkvyofficial.org/\n\n - **National Education Policy (NEP) 2020**: A comprehensive policy aimed at transforming India's education system. It integrates vocational and skill-based learning into the mainstream curriculum from an early age.\n Link: https://www.education.gov.in/nep",
        'digital_india_intro': "🇮🇳 Digital India",
        'digital_india_content': "The Digital India program aims to transform India into a digitally empowered society and a knowledge economy. Key initiatives include:\n\n - **DigiLocker**: Provides a digital space for citizens to store and access their official documents securely.\n - **BharatNet**: Aims to provide high-speed internet connectivity to all Gram Panchayats.",
        'make_in_india_intro': "🇮🇳 Make in India",
        'make_in_india_content': "The 'Make in India' initiative encourages companies to manufacture their products in India. The goal is to boost economic growth, create jobs, and attract foreign investment.",
        'emergency_intro': "🚨 Emergency and Helpline Support",
        'emergency_content': "In case of an emergency, you can use these helpline numbers:\n\n - **All-in-one Emergency Number**: **112** (Police, Fire, Ambulance)\n - **Police**: **100**\n - **Fire**: **101**\n - **Ambulance**: **108**\n - **Disaster Management**: **1078**\n - **Women's Helpline**: **1091**\n - **Kisan Call Centre (for farmers)**: **1800-180-1551**",
        'creator': "This chatbot was made by Group 7.",
        'help_text': "Here are the available commands:\n- 'info': Learn about Digital Literacy.\n- 'security': Get online security tips.\n- 'quiz': Test your knowledge.\n- 'agri': Info on agriculture schemes.\n- 'health': Info on health schemes.\n- 'skills': Info on education initiatives.\n- 'sanitation': Learn about sanitation.\n- 'emergency': Get helpline numbers.\n- 'digital_india': About the initiative.\n- 'make_in_india': About the initiative.\n- 'joke': Get a random joke.\n- 'image': Generate an image (simulation).\n- 'time': Get the current time.\n- 'date': Get today's date.\n- 'weather': Get the weather in Lucknow.\n- 'creator': See who made this chatbot.",
        'log_message': "User question logged."
    },
    'hi': {
        'title': "डिजिटल साक्षरता चैटबॉट",
        'lang_select_prompt': "चैटबॉट के लिए एक भाषा चुनें:",
        'lang_desc': "हिंदी (Hindi)",
        'welcome': "नमस्ते! मैं आपका डिजिटल साक्षरता चैटबॉट हूँ, जिसे ग्रुप 7 ने बनाया है। मैं आपको ऑनलाइन सुरक्षा और कौशल के बारे में जानने में मदद कर सकता हूँ। सभी उपलब्ध कमांड देखने के लिए 'help' टाइप करें।",
        'info_intro': "🌐 डिजिटल साक्षरता क्या है?",
        'info_content': "डिजिटल साक्षरता का अर्थ है कंप्यूटर, मोबाइल और इंटरनेट जैसे डिजिटल उपकरणों का सही उपयोग करना। यह हमें ऑनलाइन सेवाओं, बैंकिंग, शिक्षा और संचार के क्षेत्र में मदद करता है।\n\nउदाहरण:\n - ऑनलाइन बैंकिंग का उपयोग\n - ईमेल भेजना\n - सुरक्षित पासवर्ड बनाना\n - साइबर सुरक्षा के नियमों का पालन करना",
        'security_tips': "🔒 ऑनलाइन सुरक्षा टिप्स",
        'security_content': "ऑनलाइन सुरक्षा के लिए साइबर सुरक्षा बहुत महत्वपूर्ण है।\n1. **ओटीपी चेतावनी**: अपना वन-टाइम पासवर्ड (ओटीपी) कभी भी किसी के साथ साझा न करें, यहां तक ​​कि बैंक कर्मचारियों के साथ भी नहीं। ओटीपी केवल आपके उपयोग के लिए है।\n2. **फिशिंग**: व्यक्तिगत जानकारी मांगने वाले संदिग्ध ईमेल या संदेशों से सावधान रहें।\n3. **मजबूत पासवर्ड**: अक्षर, अंक और विशेष चिन्ह का मिश्रण उपयोग करें।\n4. **सार्वजनिक वाई-फाई**: सार्वजनिक वाई-फाई नेटवर्क पर संवेदनशील लेनदेन (जैसे बैंकिंग) से बचें।",
        'quiz_intro': "📝 चलिए एक छोटा सा क्विज़ करते हैं:\n",
        'q1': "1️⃣ सवाल: मजबूत पासवर्ड में क्या होना चाहिए?",
        'q1_options': "a) केवल नाम\nb) अक्षर, अंक और विशेष चिन्ह का मिश्रण\nc) जन्मतिथि",
        'q1_ans': 'b',
        'q2': "2️⃣ सवाल: अनजान व्यक्ति द्वारा भेजे गए लिंक पर क्या करना चाहिए?",
        'q2_options': "a) तुरंत क्लिक करें\nb) नजरअंदाज करें\nc) उसे सबको भेज दें",
        'q2_ans': 'b',
        'q3': "3️⃣ सवाल: क्या आपको अपना ओटीपी बैंक प्रतिनिधि के साथ साझा करना चाहिए?",
        'q3_options': "a) हाँ\nb) नहीं, कभी नहीं\nc) केवल तभी जब वे आपको बैंक नंबर से कॉल करें",
        'q3_ans': 'b',
        'q4': "4️⃣ सवाल: फिशिंग क्या है?",
        'q4_options': "a) तालाब में मछली पकड़ना\nb) फर्जी ईमेल का उपयोग करके व्यक्तिगत जानकारी चुराने की कोशिश\nc) एक प्रकार का ऑनलाइन खेल",
        'q4_ans': 'b',
        'q5': "5️⃣ सवाल: क्या सार्वजनिक वाई-फाई पर ऑनलाइन बैंकिंग करना सुरक्षित है?",
        'q5_options': "a) हाँ\nb) नहीं, यह जोखिम भरा है\nc) केवल तभी जब वाई-फाई मुफ़्त हो",
        'q5_ans': 'b',
        'correct': "सही! ✅",
        'incorrect': "गलत। ❌ सही उत्तर है: ",
        'your_score': "🎉 आपका अंतिम स्कोर: ",
        'quiz_end_excellent': "बहुत बढ़िया! आप डिजिटल साक्षरता के विशेषज्ञ हैं।",
        'quiz_end_good': "आप सही रास्ते पर हैं! थोड़ा और अभ्यास आपको विशेषज्ञ बना देगा।",
        'quiz_end_average': "सीखते रहें! अभ्यास से ही सब कुछ संभव है।",
        'nlp_positive': "आपकी प्रतिक्रिया बहुत सराहनिय है! सकारात्मक शब्दों के लिए धन्यवाद। 😊",
        'nlp_negative': "मुझे यह सुनकर खेद है। मैं आपकी बेहतर सहायता कैसे कर सकता हूँ? 🤔",
        'nlp_neutral': "ठीक है, मैं समझता हूँ। यदि आपके कोई प्रश्न हैं, तो पूछने में संकोच न करें। 🧐",
        'unknown_command': "मुझे खेद है, मुझे वह समझ में नहीं आया। उपलब्ध कमांड की सूची देखने के लिए 'help' टाइप करें।",
        'otp_warning': "🚫 सुरक्षा चेतावनी: ऐसा लगता है कि आपने ओटीपी का उल्लेख किया है। याद रखें, अपना वन-टाइम पासवर्ड किसी के साथ साझा न करें, भले ही वे बैंक या किसी अन्य सेवा से होने का दावा करें। ऑनलाइन सुरक्षित रहें!",
        'time': "वर्तमान समय है: ",
        'date': "आज की तारीख है: ",
        'weather': "लखनऊ में वर्तमान मौसम: {weather_desc}",
        'image_prompt': "कृपया उस चित्र का वर्णन करें जिसे आप मुझसे बनवाना चाहते हैं।",
        'image_generating': "🎨 आपका चित्र बनाया जा रहा है: '{prompt}'। इसमें कुछ समय लग सकता है...",
        'image_link': "🖼️ आपका चित्र तैयार है! इसे यहां देखें: ",
        'joke_intro': "😂 आपके लिए एक चुटकुला है:",
        'jokes': [
            "पुलिस वाले ने चोर से कहा, 'तुम्हारे पास जूते क्यों नहीं हैं?' चोर बोला, 'मैं भागते समय जूते क्यों पहनूँ?'",
            "टीचर: 'तुम रोज स्कूल क्यों नहीं आते?' विद्यार्थी: 'सर, मैं रोज आता हूँ, पर मेरा दिमाग घर पर रह जाता है!'",
            "गोलू: 'यार, मैं अपनी बीवी के लिए क्या खरीदूँ?' मोलू: 'तेरे पास कौन सा फोन है?' गोलू: 'iPhone 15 Pro Max' मोलू: 'तो फिर अपनी बीवी के लिए iPhone 16 Pro Max खरीद ले!'",
            "एक आदमी ने अपनी बीवी से कहा, 'मैं घर छोड़ कर जा रहा हूँ!' बीवी बोली, 'तो ठीक है, मैं भी घर छोड़ कर जा रही हूँ!' आदमी: 'तो मैं कहाँ जाऊँ?'"
        ],
        'agri_intro': "🌾 कृषि और सरकारी योजनाएँ",
        'agri_content': "कृषि पौधों और पशुओं की खेती का विज्ञान और अभ्यास है। यहां कुछ महत्वपूर्ण सरकारी योजनाएं हैं जो किसानों की मदद करती हैं:\n\n - **प्रधान मंत्री किसान सम्मान निधि (PM-KISAN)**: किसानों के लिए एक आय सहायता योजना।\n लिंक: https://pmkisan.gov.in/\n\n - **प्रधान मंत्री फसल बीमा योजना (PMFBY)**: किसानों को नुकसान से बचाने के लिए एक फसल बीमा योजना।\n लिंक: https://pmfby.gov.in/\n\n - **किसान क्रेडिट कार्ड (KCC)**: किसानों को समय पर ऋण प्रदान करने की एक योजना।\n लिंक: https://www.india.gov.in/schemes-kisan-credit-card-scheme\n\n - **प्रधान मंत्री कृषि सिंचाई योजना (PMKSY)**: देश के हर खेत को सुनिश्चित सिंचाई प्रदान करने का लक्ष्य रखती है।\n लिंक: https://pmksy.gov.in/\n\n - **गोबरधन (GOBARdhan) योजना**: ग्रामीण क्षेत्रों के लिए 'कचरे से धन' की पहल, जिसमें ठोस कचरे और गोबर को बायोगैस और जैविक खाद जैसे उपयोगी संसाधनों में परिवर्तित किया जाता है।\n लिंक: https://sbm.gov.in/gbdhn/index",
        'health_intro': "🏥 स्वास्थ्य परामर्श और योजनाएँ",
        'health_content': "आप स्वास्थ्य परामर्श कैसे प्राप्त कर सकते हैं और सरकारी स्वास्थ्य योजनाओं के बारे में जानकारी यहाँ दी गई है:\n\n - **eSanjeevani**: भारत सरकार की एक राष्ट्रीय टेलीमेडिसिन सेवा जो मुफ्त ऑनलाइन डॉक्टर परामर्श प्रदान करती है।\n लिंक: https://esanjeevani.mohfw.gov.in/\n\n - **आयुष्मान भारत - प्रधान मंत्री जन आरोग्य योजना (PM-JAY)**: दुनिया की सबसे बड़ी स्वास्थ्य आश्वासन योजना जो गरीब और कमजोर परिवारों के लिए प्रति वर्ष प्रति परिवार ₹5 लाख का स्वास्थ्य कवर प्रदान करती है।\n लिंक: https://nha.gov.in/PM-JAY",
        'sanitation_intro': "🚽 स्वच्छता जागरूकता",
        'sanitation_content': "समुदाय के स्वास्थ्य के लिए स्वच्छता जागरूकता महत्वपूर्ण है। भारत सरकार ने स्वच्छता और सफाई को बढ़ावा देने के लिए एक बड़ा अभियान शुरू किया है।\n\n - **स्वच्छ भारत मिशन (SBM)**: खुले में शौच को खत्म करने और ठोस कचरा प्रबंधन में सुधार के लिए एक राष्ट्रव्यापी अभियान। यह ग्रामीण और शहरी दोनों क्षेत्रों में शौचालय बनाने के लिए वित्तीय सहायता प्रदान करता है।\n लिंक: https://swachhbharatmission.gov.in/\n\n - **राष्ट्रीय स्वास्थ्य मिशन (NHM) की भूमिका**: NHM का ध्यान स्वास्थ्य परिणामों को बेहतर बनाने पर है, जो सीधे स्वच्छता और सफाई से जुड़े हैं। यह बीमारियों को रोकने के लिए स्वस्थ स्वच्छता प्रथाओं के बारे में जागरूकता पैदा करने का काम करता है।",
        'skills_intro': "🎓 कौशल और शिक्षा",
        'skills_content': "व्यक्तिगत विकास और राष्ट्र की प्रगति के लिए कौशल विकास और शिक्षा आवश्यक हैं। यहाँ कुछ प्रमुख सरकारी पहल हैं:\n\n - **प्रधान मंत्री कौशल विकास योजना (PMKVY)**: भारतीय युवाओं की बड़ी संख्या को उद्योग-प्रासंगिक कौशल प्रशिक्षण लेने में सक्षम बनाने की प्रमुख योजना ताकि वे बेहतर आजीविका सुरक्षित कर सकें।\n लिंक: https://pmkvyofficial.org/\n\n - **राष्ट्रीय शिक्षा नीति (NEP) 2020**: भारत की शिक्षा प्रणाली को बदलने के उद्देश्य से एक व्यापक नीति। यह कम उम्र से ही व्यावसायिक और कौशल-आधारित शिक्षा को मुख्यधारा के पाठ्यक्रम में एकीकृत करती है।\n लिंक: https://www.education.gov.in/nep",
        'digital_india_intro': "🇮🇳 डिजिटल इंडिया",
        'digital_india_content': "डिजिटल इंडिया कार्यक्रम का उद्देश्य भारत को एक डिजिटल रूप से सशक्त समाज और ज्ञान अर्थव्यवस्था में बदलना है। मुख्य पहलों में शामिल हैं:\n\n - **डिजी लॉकर (DigiLocker)**: नागरिकों को अपने आधिकारिक दस्तावेजों को सुरक्षित रूप से संग्रहीत करने और उन तक पहुँचने के लिए एक डिजिटल स्थान प्रदान करता है।\n - **भारतनेट (BharatNet)**: सभी ग्राम पंचायतों को हाई-स्पीड इंटरनेट कनेक्टिविटी प्रदान करने का लक्ष्य रखता है।",
        'make_in_india_intro': "🇮🇳 मेक इन इंडिया",
        'make_in_india_content': "'मेक इन इंडिया' पहल कंपनियों को भारत में अपने उत्पादों का निर्माण करने के लिए प्रोत्साहित करती है। इसका लक्ष्य आर्थिक विकास को बढ़ावा देना, रोजगार पैदा करना और विदेशी निवेश को आकर्षित करना है।",
        'emergency_intro': "🚨 आपातकालीन और हेल्पलाइन सहायता",
        'emergency_content': "आपात स्थिति में, आप इन हेल्पलाइन नंबरों का उपयोग कर सकते हैं:\n\n - **ऑल-इन-वन आपातकालीन नंबर**: **112** (पुलिस, अग्निशमन, एम्बुलेंस)\n - **पुलिस**: **100**\n - **अग्निशमन**: **101**\n - **एम्बुलेंस**: **108**\n - **आपदा प्रबंधन**: **1078**\n - **महिला हेल्पलाइन**: **1091**\n - **किसान कॉल सेंटर (किसानों के लिए)**: **1800-180-1551**",
        'creator': "इस चैटबॉट को ग्रुप 7 ने बनाया है।",
        'help_text': "यहां उपलब्ध कमांड हैं:\n- 'info': डिजिटल साक्षरता के बारे में जानें।\n- 'security': ऑनलाइन सुरक्षा युक्तियाँ प्राप्त करें।\n- 'quiz': अपने ज्ञान का परीक्षण करें।\n- 'agri': कृषि योजनाओं पर जानकारी।\n- 'health': स्वास्थ्य योजनाओं पर जानकारी।\n- 'skills': शिक्षा पहलों पर जानकारी।\n- 'sanitation': स्वच्छता के बारे में जानें।\n- 'emergency': हेल्पलाइन नंबर प्राप्त करें।\n- 'digital_india': पहल के बारे में।\n- 'make_in_india': पहल के बारे में।\n- 'joke': एक चुटकुला प्राप्त करें।\n- 'image': एक छवि उत्पन्न करें (सिमुलेशन)।\n- 'time': वर्तमान समय प्राप्त करें।\n- 'date': आज की तारीख प्राप्त करें।\n- 'weather': लखनऊ में मौसम जानें।\n- 'creator': देखें कि यह चैटबॉट किसने बनाया।",
        'log_message': "उपयोगकर्ता का प्रश्न लॉग किया गया।"
    },
    # --- Other languages omitted for brevity but are present in the full code structure ---
    # Hinglish, Awadhi, Gujarati, and the NEW languages: Bengali, Tamil, Marathi
    # All languages follow the same structure and have been fully translated.
    'hing': {
        'title': "डिजिटल लिटरेसी चैटबॉट (Hinglish)",
        'lang_select_prompt': "Chatbot ke liye ek language choose karo:",
        'lang_desc': "Hinglish (Hindi + English)",
        'welcome': "Hello! Main aapka Digital Literacy Chatbot hoon, jise Group 7 ne banaya hai. Main aapko online safety aur skills sikhane mein help kar sakta hoon. 'help' type karke saare available commands dekho.",
        'info_intro': "🌐 Digital Literacy kya hai?",
        'info_content': "Digital literacy ka matlab hai computer, mobile, aur internet jaise digital devices ko sahi tarike se use karna. Isse hum online services, banking, education aur communication mein help milti hai.\n\nExamples:\n - Online banking use karna\n - Emails send karna\n - Strong passwords banana\n - Cybersecurity rules follow karna",
        'security_tips': "🔒 Online Security Tips",
        'security_content': "Cybersecurity online safety ke liye bahut important hai.\n1. **OTP Warning**: Apna One-Time Password (OTP) kabhi bhi kisi ke saath share mat karo, bank employees ke saath bhi nahi. OTP sirf aapke use ke liye hai.\n2. **Phishing**: Suspicious emails ya messages se savdhan raho jo personal information maange.\n3. **Strong Passwords**: Letters, numbers, aur special characters ka mix use karo.\n4. **Public Wi-Fi**: Public Wi-Fi networks par sensitive transactions (jaise banking) avoid karo.",
        'quiz_intro': "📝 Chalo ek quick quiz karte hain:\n",
        'q1': "1️⃣ Question: Strong password mein kya hona chahiye?",
        'q1_options': "a) Sirf names\nb) Letters, numbers, aur special characters ka mix\nc) Date of birth",
        'q1_ans': 'b',
        'q2': "2️⃣ Question: Ek unknown person ke bheje hue link ka kya karna chahiye?",
        'q2_options': "a) Uspe turant click karo\nb) Usko ignore karo\nc) Usko sabke saath share karo",
        'q2_ans': 'b',
        'q3': "3️⃣ Question: Kya aapko apna OTP bank representative ke saath share karna chahiye?",
        'q3_options': "a) Yes\nb) No, bilkul nahi\nc) Only agar wo bank number se call kare",
        'q3_ans': 'b',
        'q4': "4️⃣ Question: Phishing kya hai?",
        'q4_options': "a) Paani mein fish pakadna\nb) Fake emails se personal information chori karne ki koshish\nc) Ek tarah ka online game",
        'q4_ans': 'b',
        'q5': "5️⃣ Question: Kya public Wi-Fi par online banking karna safe hai?",
        'q5_options': "a) Yes\nb) No, bilkul risky hai\nc) Sirf agar Wi-Fi free ho to",
        'q5_ans': 'b',
        'correct': "Correct! ✅",
        'incorrect': "Incorrect. ❌ Sahi jawab hai: ",
        'your_score': "🎉 Aapka final score: ",
        'quiz_end_excellent': "Great job! Aap ek digital literacy expert ho.",
        'quiz_end_good': "Aap sahi track par ho! Thoda aur practice aapko expert bana dega.",
        'quiz_end_average': "Seekhte raho! Practice makes perfect.",
        'nlp_positive': "Aapka feedback bahut accha laga! Positive words ke liye thanks. 😊",
        'nlp_negative': "I'm sorry to hear that. Main kaise aur better help kar sakta hoon? 🤔",
        'nlp_neutral': "Okay, main samajh gaya. Agar koi aur sawal ho to pooch sakte ho. 🧐",
        'unknown_command': "I'm sorry, main yeh command nahi samjha. Available commands ki list dekhne ke liye 'help' type karo.",
        'otp_warning': "🚫 SECURITY ALERT: Aisa lagta hai ki aapne OTP mention kiya hai. Yaad rakho, apna One-Time Password kisi ke saath share mat karo, bhale hi wo bank ya kisi aur service se hone ka daava kare. Online safe raho!",
        'time': "Current time hai: ",
        'date': "Aaj ka date hai: ",
        'weather': "Lucknow mein current weather: {weather_desc}",
        'image_prompt': "Please describe karo ki aap kaun si image generate karwana chahte ho.",
        'image_generating': "🎨 Aapki image generate ho rahi hai: '{prompt}'. Isme thoda time lag sakta hai...",
        'image_link': "🖼️ Aapki image ready hai! Yahan dekho: ",
        'joke_intro': "😂 Yeh lo ek joke:",
        'jokes': [
            "Pappu: 'Mummy, main kitna badmaash hoon?' Mummy: 'Pagal hai, tu to sher hai!' Pappu: 'To school mein ma'am mujhe chuha kyu kehti hai?'",
            "Teacher: 'Tumhara homework kahan hai?' Student: 'Sir, wo to kal hi ho gaya tha.' Teacher: 'To aaj kyu nahi hai?' Student: 'Sir, main roz-roz thodi na karta hoon!'",
            "Ek machhar ne doosre se kaha, 'Yaar, bahut garmi hai!' Doosra bola, 'To khet mein chalo, wahan AC hai.'",
            "Ek aadmi ne apni biwi se kaha, 'Main ghar chhod kar ja raha hoon!' Biwi boli, 'To theek hai, main bhi ghar chhod kar ja rahi hoon!' Aadmi: 'To main kahan jaaun?'"
        ],
        'agri_intro': "🌾 Agriculture aur Government Schemes",
        'agri_content': "Agriculture plants aur livestock ko cultivate karne ka science aur practice hai. Farmers ki help ke liye kuch important Government schemes hain:\n\n - **Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)**: Farmers ke liye ek income support scheme hai.\n Link: https://pmkisan.gov.in/\n\n - **Pradhan Mantri Fasal Bima Yojana (PMFBY)**: Farmers ko loss se bachane ke liye ek crop insurance scheme hai.\n Link: https://pmfby.gov.in/\n\n - **Kisan Credit Card (KCC)**: Farmers ko time par credit dene ki scheme.\n Link: https://www.india.gov.in/schemes-kisan-credit-card-scheme\n\n - **Pradhan Mantri Krishi Sinchai Yojana (PMKSY)**: Iska aim hai country ke har farm ko assured irrigation provide karna.\n Link: https://pmksy.gov.in/\n\n - **GOBARdhan Scheme**: Rural areas ke liye ek 'Waste to Wealth' initiative, jisse solid waste aur cattle dung ko biogas aur organic manure jaise useful resources mein convert kiya jaata hai.\n Link: https://sbm.gov.in/gbdhn/index",
        'health_intro': "🏥 Health Consultation aur Schemes",
        'health_content': "Aap health consultations aur government health schemes ke baare mein yahan se information le sakte hain:\n\n - **eSanjeevani**: Government of India ki ek national telemedicine service hai jo free online doctor consultations deti hai.\n Link: https://esanjeevani.mohfw.gov.in/\n\n - **Ayushman Bharat - Pradhan Mantri Jan Arogya Yojana (PM-JAY)**: Duniya ki sabse badi health assurance scheme jo gareeb aur vulnerable families ko saal bhar ₹5 lakh tak ka health cover deti hai.\n Link: https://nha.gov.in/PM-JAY",
        'sanitation_intro': "🚽 Sanitation Awareness",
        'sanitation_content': "Community health ke liye sanitation awareness bahut important hai. Government of India ne cleanliness aur hygiene ko promote karne ke liye ek bada campaign launch kiya hai.\n\n - **Swachh Bharat Mission (SBM)**: Open defecation ko eliminate karne aur solid waste management ko improve karne ke liye ek nationwide campaign. Ye rural aur urban dono areas mein toilets banane ke liye financial assistance deta hai.\n Link: https://swachhbharatmission.gov.in/\n\n - **National Health Mission (NHM) ka Role**: NHM health outcomes ko improve karne par focus karta hai, jo directly sanitation aur hygiene se linked hain. Ye diseases ko prevent karne ke liye healthy sanitation practices ke baare mein awareness create karta hai.",
        'skills_intro': "🎓 Skills aur Education",
        'skills_content': "Individual growth aur national progress ke liye skill development aur education bahut zaruri hain. Yahan kuch main government initiatives hain:\n\n - **Pradhan Mantri Kaushal Vikas Yojana (PMKVY)**: Indian youth ki ek badi population ko industry-relevant skill training dene ki flagship scheme taaki unki livelihood better ho sake.\n Link: https://pmkvyofficial.org/\n\n - **National Education Policy (NEP) 2020**: India ke education system ko transform karne ke liye ek comprehensive policy. Ye vocational aur skill-based learning ko early age se hi mainstream curriculum mein integrate karti hai.\n Link: https://www.education.gov.in/nep",
        'digital_india_intro': "🇮🇳 Digital India",
        'digital_india_content': "Digital India program ka aim hai India ko ek digitally empowered society aur knowledge economy mein badalna. Main initiatives hain:\n\n - **DigiLocker**: Citizens ko unke official documents ko secure tarike se store aur access karne ke liye ek digital space deta hai.\n - **BharatNet**: Sabhi Gram Panchayats ko high-speed internet connectivity provide karne ka aim hai.",
        'make_in_india_intro': "🇮🇳 Make in India",
        'make_in_india_content': "'Make in India' initiative companies ko India mein apne products manufacture karne ke liye encourage karta hai. Iska goal hai economic growth ko boost karna, jobs create karna, aur foreign investment attract karna.",
        'emergency_intro': "🚨 Emergency aur Helpline Support",
        'emergency_content': "Emergency ke case mein, aap in helpline numbers ka use kar sakte hain:\n\n - **All-in-one Emergency Number**: **112** (Police, Fire, Ambulance)\n - **Police**: **100**\n - **Fire**: **101**\n - **Ambulance**: **108**\n - **Disaster Management**: **1078**\n - **Women's Helpline**: **1091**\n - **Kisan Call Centre (farmers ke liye)**: **1800-180-1551**",
        'creator': "Is chatbot ko Group 7 ne banaya hai.",
        'help_text': "Yeh rahe available commands:\n- 'info': Digital Literacy ke baare mein jaano.\n- 'security': Online security tips lo.\n- 'quiz': Apna knowledge test karo.\n- 'agri': Agriculture schemes ki jaankari.\n- 'health': Health schemes ki jaankari.\n- 'skills': Education initiatives ki jaankari.\n- 'sanitation': Sanitation ke baare mein jaano.\n- 'emergency': Helpline numbers dekho.\n- 'digital_india': Is initiative ke baare mein.\n- 'make_in_india': Is initiative ke baare mein.\n- 'joke': Ek random joke suno.\n- 'image': Ek image generate karo (simulation).\n- 'time': Current time dekho.\n- 'date': Aaj ki date dekho.\n- 'weather': Lucknow ka weather jaano.\n- 'creator': Dekho is chatbot ko kisne banaya.",
        'log_message': "User ka question log ho gaya."
    },
    'awa': {
        'title': "डिजिटल साक्षरता चैटबॉट (अवधी)",
        'lang_select_prompt': "चैटबॉट खातिर एक भाषा चुना:",
        'lang_desc': "अवधी (Awadhi)",
        'welcome': "जय सियाराम! हम तुहार डिजिटल साक्षरता चैटबॉट हईं, जेका ग्रुप 7 बनाइस हय। हम तोहार ऑनलाइन सुरक्षा अउर हुनर सीखे में मदद कइ सकित हईं। सब कमांड देखे खातिर 'help' टाइप करा।",
        'info_intro': "🌐 डिजिटल साक्षरता का हय?",
        'info_content': "डिजिटल साक्षरता का मतलब कंप्यूटर, मोबाइल, अउर इंटरनेट जइसे डिजिटल औज़ारन का सही उपयोग करब हय। इ हमका ऑनलाइन सेवा, बैंक का काम, पढ़ाई अउर बात-चीत करे में मदद करइ हय।\n\nउदाहरण:\n - ऑनलाइन बैंकिंग का उपयोग\n - ईमेल भेजइ\n - मजबूत पासवर्ड बनउब\n - साइबर सुरक्षा का नियम मानइ",
        'security_tips': "🔒 ऑनलाइन सुरक्षा",
        'security_content': "ऑनलाइन सुरक्षित रहे खातिर साइबर सुरक्षा बहुत जरूरी हय।\n1. **ओटीपी चेतावनी**: आपन वन-टाइम पासवर्ड (ओटीपी) केहू से न बतावा, चाहे उ बैंक के कर्मचारी ही काहें न होए। ओटीपी खाली तोहार उपयोग खातिर हय।\n2. **फिशिंग**: अइसे संदिग्ध ईमेल या संदेशन से बचि के रहा जे तोहार निजी जानकारी माँगे।\n3. **मजबूत पासवर्ड**: अक्षर, अंक, अउर खास चिन्हन का मेल उपयोग करा।\n4. **पब्लिक वाई-फाई**: पब्लिक वाई-फाई नेटवर्क पर संवेदनशील काम (जइसे बैंकिंग) करे से बची।",
        'quiz_intro': "📝 चला, एक ठौ छोटका क्विज़ करा जा:\n",
        'q1': "1️⃣ सवाल: एक मजबूत पासवर्ड में का होए चाही?",
        'q1_options': "a) खाली नाम\nb) अक्षर, अंक, अउर खास चिन्हन का मेल\nc) जनम तिथि",
        'q1_ans': 'b',
        'q2': "2️⃣ सवाल: अनजान मनई के भेजल लिंक पर का करब चाही?",
        'q2_options': "a) झट से ओपर क्लिक करा\nb) ओका छोड़ि द्या\nc) सबरे के साथ शेयर करा",
        'q2_ans': 'b',
        'q3': "3️⃣ सवाल: का तोहे आपन ओटीपी बैंक के आदमी से बतावब चाही?",
        'q3_options': "a) हाँ\nb) नाहीं, कबहुँ नाहीं\nc) खाली तब जब उ बैंक के नंबर से फोन करे",
        'q3_ans': 'b',
        'q4': "4️⃣ सवाल: फिशिंग का हय?",
        'q4_options': "a) पोखरा में मछरी पकड़ब\nb) फर्जी ईमेल का उपयोग कइके निजी जानकारी चोरइ का प्रयास\nc) एक तरह का ऑनलाइन खेल",
        'q4_ans': 'b',
        'q5': "5️⃣ सवाल: का सार्वजनिक वाई-फाई पर ऑनलाइन बैंकिंग करब सुरक्षित हय?",
        'q5_options': "a) हाँ\nb) नाहीं, इ खतरा भरा हय\nc) खाली तब जब वाई-फाई मुफ्त होय",
        'q5_ans': 'b',
        'correct': "सही हय! ✅",
        'incorrect': "गलत हय। ❌ सही उत्तर हय: ",
        'your_score': "🎉 तोहार आखिरी स्कोर: ",
        'quiz_end_excellent': "बहूत बढ़िया! आप डिजिटल साक्षरता के गुरु हउवा।",
        'quiz_end_good': "आप सही रास्ता पर हउवा! थोड़ि अउर अभ्यास तोहे गुरु बनाइ देई।",
        'quiz_end_average': "सीखत रहा! अभ्यास से सब कुछ बन जाइ हय।",
        'nlp_positive': "तोहार प्रतिक्रिया बहुत बढ़िया लागत हय! सकारात्मक शब्दन खातिर धन्यवाद्। 😊",
        'nlp_negative': "हमका इ सुनि के खेद हय। हम तोहार अउर अच्छा मदद कइसे कइ सकित हईं? 🤔",
        'nlp_neutral': "ठीक हय, हम समझि गइलीं। अगर तोहार कउनो अउर सवाल होए, तो पूछी सकित हउवा। 🧐",
        'unknown_command': "हमका खेद हय, हम इ नाहीं समझि पाइल। उपलब्ध कमांड देखे खातिर 'help' टाइप करा।",
        'otp_warning': "🚫 सुरक्षा चेतावनी: लागत हय कि तू ओटीपी का जिक्र कइले हउवा। याद रखा, आपन वन-टाइम पासवर्ड केहू से ना बतावा, चाहे उ बैंक या कउनो दूसर सेवा से होय का दावा करे। ऑनलाइन सुरक्षित रहा!",
        'time': "वर्तमान समय हय: ",
        'date': "आज के तारीख हय: ",
        'weather': "लखनऊ में वर्तमान मौसम: {weather_desc}",
        'image_prompt': "कृपया उ चित्र का वर्णन करा जे तोहे बनवावब हय।",
        'image_generating': "🎨 तोहार चित्र बनइ रहल हय: '{prompt}'। इमे कुछ समय लाग सकत हय...",
        'image_link': "🖼️ तोहार चित्र तैयार हय! इहाँ देखा: ",
        'joke_intro': "😂 तोहार खातिर एक चुटकुला हय:",
        'jokes': [
            "पुलिस वाले चोर से कहले, 'तोहार लगे जूता काहे नाहीं हय?' चोर कहले, 'हम भागते समय जूता काहे पहनीं?'",
            "गुरुजी: 'तू रोज स्कूल काहे नाहीं आवत?' लरिका: 'गुरुजी, हम रोज आवत हईं, लेकिन हमार दिमाग घरै छूट जात हय!'",
            "गोलू: 'यार, हम आपन मेहरारु खातिर का खरीदीं?' मोलू: 'तोहार लगे कवन मोबाइल हय?' गोलू: 'iPhone 15 Pro Max' मोलू: 'तो आपन मेहरारु खातिर iPhone 16 Pro Max लेइ ल्या!'",
            "एक मनई आपन मेहरारु से कहले, 'हम घर छोडि के जात हई!' मेहरारु कहलस, 'तो ठीक हय, हम भी घर छोडि के जात हई!' मनई: 'तो हम कहाँ जाई?'"
        ],
        'agri_intro': "🌾 कृषि अउर सरकारी योजनाएँ",
        'agri_content': "कृषि पौध अउर जानवरन के खेती का विज्ञान अउर काम हय। इहाँ कुछ महत्वपूर्ण सरकारी योजनाएँ हइन जे किसानन के मदद करत हइन:\n\n - **प्रधान मंत्री किसान सम्मान निधि (PM-KISAN)**: किसानन खातिर एक आय सहायता योजना।\n लिंक: https://pmkisan.gov.in/\n\n - **प्रधान मंत्री फसल बीमा योजना (PMFBY)**: किसानन के नुकसान से बचावे खातिर एक फसल बीमा योजना।\n लिंक: https://pmfby.gov.in/\n\n - **किसान क्रेडिट कार्ड (KCC)**: किसानन के समय पर ऋण देवे का एक योजना।\n लिंक: https://www.india.gov.in/schemes-kisan-credit-card-scheme\n\n - **प्रधान मंत्री कृषि सिंचाई योजना (PMKSY)**: देस के हर खेत के सुनिश्चित सिंचाई देवे का लक्ष्य रखत हय।\n लिंक: https://pmksy.gov.in/\n\n - **गोबरधन (GOBARdhan) योजना**: ग्रामीण इलाकन खातिर 'कचरे से धन' का पहल, जेमे ठोस कचरा अउर गोबर का उपयोग करके बायोगैस अउर जैविक खाद जइसे उपयोगी संसाधन बनउल जाइ हय।\n लिंक: https://sbm.gov.in/gbdhn/index",
        'health_intro': "🏥 स्वास्थ्य परामर्श अउर योजनाएँ",
        'health_content': "आप स्वास्थ्य परामर्श कइसे प्राप्त कइ सकित हउवा अउर सरकारी स्वास्थ्य योजनान के बारे में जानकारी इहाँ दीन्ह गयल हय:\n\n - **eSanjeevani**: भारत सरकार के एक राष्ट्रीय टेलीमेडिसिन सेवा जे मुफ्त ऑनलाइन डॉक्टर परामर्श देत हय।\n लिंक: https://esanjeevani.mohfw.gov.in/\n\n - **आयुष्मान भारत - प्रधान मंत्री जन आरोग्य योजना (PM-JAY)**: दुनिया के सबसे बड़ स्वास्थ्य आश्वासन योजना जे गरीब अउर कमजोर परिवारन खातिर प्रति वर्ष प्रति परिवार ₹5 लाख का स्वास्थ्य कवर देत हय।\n लिंक: https://nha.gov.in/PM-JAY",
        'sanitation_intro': "🚽 स्वच्छता जागरूकता",
        'sanitation_content': "समुदाय के स्वास्थ्य खातिर स्वच्छता जागरूकता जरूरी हय। भारत सरकार सफाई अउर स्वच्छता के बढ़ावा देवे खातिर एक बड़ अभियान चलाइले हय।\n\n - **स्वच्छ भारत मिशन (SBM)**: खुले में शौच का खतम करे अउर ठोस कचरा प्रबंधन के सुधारे खातिर एक देस-व्यापी अभियान। इ ग्रामीण अउर शहरी दुइनो इलाकन में शौचालय बनउवे खातिर आर्थिक मदद देत हय।\n लिंक: https://swachhbharatmission.gov.in/\n\n - **राष्ट्रीय स्वास्थ्य मिशन (NHM) के भूमिका**: NHM का ध्यान स्वास्थ्य का परिणाम सुधारे पर हय, जे सीधा स्वच्छता अउर सफाई से जुड़ल हय। इ बीमारी के रोके खातिर स्वस्थ स्वच्छता का आदत के बारे में जागरूकता पैदा करइ हय।",
        'skills_intro': "🎓 कौशल अउर शिक्षा",
        'skills_content': "व्यक्तिगत विकास अउर राष्ट्र के प्रगति खातिर कौशल विकास अउर शिक्षा जरूरी हय। इहाँ कुछ प्रमुख सरकारी पहल हइन:\n\n - **प्रधान मंत्री कौशल विकास योजना (PMKVY)**: भारतीय जवानन के एक बड़ संख्या के उद्योग से जुड़ल कौशल प्रशिक्षण देवे का मुख्य योजना ताकि उ एक अच्छा आजीविका सुरक्षित कइ सकइ।\n लिंक: https://pmkvyofficial.org/\n\n - **राष्ट्रीय शिक्षा नीति (NEP) 2020**: भारत के शिक्षा प्रणाली के बदले का मकसद से एक व्यापक नीति। इ कम उम्र से ही व्यावसायिक अउर कौशल-आधारित शिक्षा के मुख्य धारा का पाठ्यक्रम में जोड़इ हय।\n लिंक: https://www.education.gov.in/nep",
        'digital_india_intro': "🇮🇳 डिजिटल इंडिया",
        'digital_india_content': "डिजिटल इंडिया कार्यक्रम का मकसद भारत के एक डिजिटल रूप से सशक्त समाज अउर ज्ञान अर्थव्यवस्था में बदलइ हय। मुख्य पहल में शामिल हइन:\n\n - **डिजी लॉकर (DigiLocker)**: नागरिकन के आपन आधिकारिक दस्तवेजन के सुरक्षित रूप से रखई अउर उन तक पहुँचइ खातिर एक डिजिटल जगह देत हय।\n - **भारतनेट (BharatNet)**: सबरे ग्राम पंचायतन के हाई-स्पीड इंटरनेट कनेक्टिविटी देवे का मकसद रखत हय।",
        'make_in_india_intro': "🇮🇳 मेक इन इंडिया",
        'make_in_india_content': "'मेक इन इंडिया' पहल कंपनियों के भारत में आपन उत्पाद बनावे खातिर प्रोत्साहित करइ हय। एकर मकसद आर्थिक विकास के बढ़ावा देब, रोजगार पैदा करब, अउर विदेशी निवेश के आकर्षित करब हय।",
        'emergency_intro': "🚨 आपातकालीन अउर हेल्पलाइन सहायता",
        'emergency_content': "आपात स्थिति में, आप इ हेल्पलाइन नंबर का उपयोग कइ सकित हउवा:\n\n - **ऑल-इन-वन आपातकालीन नंबर**: **112** (पुलिस, अग्निशमन, एम्बुलेंस)\n - **पुलिस**: **100**\n - **अग्निशमन**: **101**\n - **एम्बुलेंस**: **108**\n - **आपदा प्रबंधन**: **1078**\n - **महिला हेल्पलाइन**: **1091**\n - **किसान कॉल सेंटर (किसानन खातिर)**: **1800-180-1551**",
        'creator': "इ चैटबॉट के ग्रुप 7 बनउले हइन।",
        'help_text': "इहाँ उपलब्ध कमांड हइन:\n- 'info': डिजिटल साक्षरता के बारे में जाना।\n- 'security': ऑनलाइन सुरक्षा सलाह ल्या।\n- 'quiz': आपन ज्ञान परखा।\n- 'agri': खेती-बाड़ी योजना के जानकारी।\n- 'health': स्वास्थ्य योजना के जानकारी।\n- 'skills': शिक्षा पहल के जानकारी।\n- 'sanitation': सफाई के बारे में जाना।\n- 'emergency': हेल्पलाइन नंबर ल्या।\n- 'digital_india': पहल के बारे में।\n- 'make_in_india': पहल के बारे में।\n- 'joke': एक चुटकुला सुना।\n- 'image': एक चित्र बनावा (सिमुलेशन)।\n- 'time': वर्तमान समय जाना।\n- 'date': आज के तारीख जाना।\n- 'weather': लखनऊ का मौसम जाना।\n- 'creator': देखा इ चैटबॉट के बनाइस हय।",
        'log_message': "उपयोगकर्ता का सवाल लॉग होइ गयल।"
    },
    'guj': {
        'title': "ડિજિટલ સાક્ષરતા ચેટબોટ",
        'lang_select_prompt': "ચેટબોટ માટે એક ભાષા પસંદ કરો:",
        'lang_desc': "ગુજરાતી (Gujarati)",
        'welcome': "નમસ્કાર! હું તમારો ડિજિટલ સાક્ષરતા ચેટબોટ છું, જે ગ્રુપ 7 દ્વારા બનાવવામાં આવ્યો છે. હું તમને ઓનલાઈન સુરક્ષા અને કૌશલ્યો વિશે શીખવામાં મદદ કરી શકું છું. બધા ઉપલબ્ધ આદેશો જોવા માટે 'help' લખો.",
        'info_intro': "🌐 ડિજિટલ સાક્ષરતા એટલે શું?",
        'info_content': "ડિજિટલ સાક્ષરતા એટલે કમ્પ્યુટર, મોબાઈલ અને ઈન્ટરનેટ જેવા ડિજિટલ ઉપકરણોનો યોગ્ય રીતે ઉપયોગ કરવાની ક્ષમતા. તે આપણને ઓનલાઈન સેવાઓ, બેંકિંગ, શિક્ષણ અને સંદેશાવ્યવહારમાં મદદ કરે છે.\n\nઉદાહરણો:\n - ઓનલાઈન બેંકિંગનો ઉપયોગ\n - ઈમેલ મોકલવા\n - મજબૂત પાસવર્ડ બનાવવા\n - સાયબર સુરક્ષાના નિયમોનું પાલન કરવું",
        'security_tips': "🔒 ઓનલાઈન સુરક્ષા ટિપ્સ",
        'security_content': "ઓનલાઈન સુરક્ષા માટે સાયબર સુરક્ષા ચાવીરૂપ છે.\n1. **OTP ચેતવણી**: તમારો વન-ટાઇમ પાસવર્ડ (OTP) ક્યારેય કોઈની સાથે શેર કરશો નહીં, બેંક કર્મચારીઓ સાથે પણ નહીં. OTP ફક્ત તમારા ઉપયોગ માટે છે.\n2. **ફિશિંગ**: શંકાસ્પદ ઇમેઇલ્સ અથવા સંદેશાઓથી સાવચેત રહો જે વ્યક્તિગત માહિતી માંગે છે.\n3. **મજબૂત પાસવર્ડ**: અક્ષરો, સંખ્યાઓ અને વિશેષ અક્ષરોનું મિશ્રણ વાપરો.\n4. **પબ્લિક વાઇ-ફાઇ**: પબ્લિક વાઇ-ફાઇ નેટવર્ક પર સંવેદનશીલ વ્યવહારો (જેમ કે બેંકિંગ) કરવાનું ટાળો.",
        'quiz_intro': "📝 ચાલો એક નાની ક્વિઝ કરીએ:\n",
        'q1': "1️⃣ પ્રશ્ન: મજબૂત પાસવર્ડમાં શું શામેલ હોવું જોઈએ?",
        'q1_options': "a) માત્ર નામો\nb) અક્ષરો, સંખ્યાઓ અને વિશેષ અક્ષરોનું મિશ્રણ\nc) જન્મતારીખ",
        'q1_ans': 'b',
        'q2': "2️⃣ પ્રશ્ન: કોઈ અજાણી વ્યક્તિ દ્વારા મોકલવામાં આવેલી લિંકનું શું કરવું જોઈએ?",
        'q2_options': "a) તેના પર તરત ક્લિક કરો\nb) તેને અવગણો\nc) તેને બધા સાથે શેર કરો",
        'q2_ans': 'b',
        'q3': "3️⃣ પ્રશ્ન: શું તમારે તમારો OTP બેંક પ્રતિનિધિ સાથે શેર કરવો જોઈએ?",
        'q3_options': "a) હા\nb) ના, ક્યારેય નહીં\nc) ફક્ત જો તેઓ તમને બેંક નંબરથી કોલ કરે તો",
        'q3_ans': 'b',
        'q4': "4️⃣ પ્રશ્ન: ફિશિંગ શું છે?",
        'q4_options': "a) તળાવમાં માછલી પકડવી\nb) નકલી ઇમેઇલ્સનો ઉપયોગ કરીને વ્યક્તિગત માહિતી ચોરી કરવાનો પ્રયાસ\nc) એક પ્રકારની ઓનલાઇન રમત",
        'q4_ans': 'b',
        'q5': "5️⃣ પ્રશ્ન: શું પબ્લિક વાઇ-ફાઇ પર ઓનલાઇન બેંકિંગ કરવું સુરક્ષિત છે?",
        'q5_options': "a) હા\nb) ના, તે જોખમી છે\nc) ફક્ત જો વાઇ-ફાઇ મફત હોય તો",
        'q5_ans': 'b',
        'correct': "સાચું! ✅",
        'incorrect': "ખોટું. ❌ સાચો જવાબ છે: ",
        'your_score': "🎉 તમારો અંતિમ સ્કોર: ",
        'quiz_end_excellent': "ખૂબ સરસ! તમે ડિજિટલ સાક્ષરતાના નિષ્ણાત છો.",
        'quiz_end_good': "તમે સાચા માર્ગ પર છો! થોડો વધુ અભ્યાસ તમને નિષ્ણાત બનાવશે.",
        'quiz_end_average': "શીખતા રહો! અભ્યાસથી બધું શક્ય બને છે.",
        'nlp_positive': "તમારા પ્રતિભાવની ખૂબ પ્રશંસા થાય છે! સકારાત્મક શબ્દો માટે આભાર. 😊",
        'nlp_negative': "આ સાંભળીને મને દુઃખ થયું. હું તમને વધુ સારી રીતે કેવી રીતે મદદ કરી શકું? 🤔",
        'nlp_neutral': "બરાબર, હું સમજું છું. જો તમને કોઈ પ્રશ્નો હોય, તો પૂછવા માટે મફત રહો. 🧐",
        'unknown_command': "માફ કરશો, હું તે સમજી શકતો નથી. ઉપલબ્ધ આદેશોની સૂચિ જોવા માટે 'help' લખો.",
        'otp_warning': "🚫 સુરક્ષા ચેતવણી: એવું લાગે છે કે તમે OTP નો ઉલ્લેખ કર્યો છે. યાદ રાખો, તમારો વન-ટાઇમ પાસવર્ડ ક્યારેય કોઈની સાથે શેર કરશો નહીં, ભલે તેઓ બેંક અથવા અન્ય કોઈ સેવાના હોવાનો દાવો કરે. ઓનલાઇન સુરક્ષિત રહો!",
        'time': "વર્તમાન સમય છે: ",
        'date': "આજની તારીખ છે: ",
        'weather': "લખનઉમાં વર્તમાન હવામાન: {weather_desc}",
        'image_prompt': "કૃપા કરીને તમે જે ચિત્ર બનાવવા માંગો છો તેનું વર્ણન કરો.",
        'image_generating': "🎨 તમારું ચિત્ર જનરેટ થઈ રહ્યું છે: '{prompt}'। આમાં થોડો સમય લાગી શકે છે...",
        'image_link': "🖼️ તમારું ચિત્ર તૈયાર છે! તેને અહીં જુઓ: ",
        'joke_intro': "😂 અહીં તમારા માટે એક જોક છે:",
        'jokes': [
            "પોલીસવાળાએ ચોરને કહ્યું, 'તારી પાસે બુટ કેમ નથી?' ચોર બોલ્યો, 'હું ભાગતી વખતે બુટ કેમ પહેરું?'",
            "ટીચર: 'તમે રોજ શાળાએ કેમ આવતા નથી?' વિદ્યાર્થી: 'સર, હું રોજ આવું છું, પણ મારું મગજ ઘરે રહી જાય છે!'",
            "ગોલુ: 'યાર, હું મારી પત્ની માટે શું ખરીદું?' મોલુ: 'તારી પાસે કયો ફોન છે?' ગોલુ: 'iPhone 15 Pro Max' મોલુ: 'તો પછી તારી પત્ની માટે iPhone 16 Pro Max ખરીદી લે!'",
            "એક માણસે પોતાની પત્નીને કહ્યું, 'હું ઘર છોડીને જઈ રહ્યો છું!' પત્ની બોલી, 'તો બરાબર, હું પણ ઘર છોડીને જઈ રહી છું!' માણસ: 'તો હું ક્યાં જાઉં?'"
        ],
        'agri_intro': "🌾 કૃષિ અને સરકારી યોજનાઓ",
        'agri_content': "કૃષિ એ છોડ અને પશુધનની ખેતીનું વિજ્ઞાન અને વ્યવહાર છે. ખેડૂતોને મદદ કરતી કેટલીક મુખ્ય સરકારી યોજનાઓ અહીં આપેલી છે:\n\n - **પ્રધાન મંત્રી કિસાન સન્માન નિધિ (PM-KISAN)**: ખેડૂતો માટે એક આવક સહાય યોજના.\n લિંક: https://pmkisan.gov.in/\n\n - **પ્રધાન મંત્રી ફસલ બીમા યોજના (PMFBY)**: ખેડૂતોને નુકસાનથી બચાવવા માટે એક પાક વીમા યોજના.\n લિંક: https://pmfby.gov.in/\n\n - **કિસાન ક્રેડિટ કાર્ડ (KCC)**: ખેડૂતોને સમયસર ધિરાણ પૂરું પાડવાની એક યોજના.\n લિંક: https://www.india.gov.in/schemes-kisan-credit-card-scheme\n\n - **પ્રધાન મંત્રી કૃષિ સિંચાઈ યોજના (PMKSY)**: દેશના દરેક ખેતરને સુનિશ્ચિત સિંચાઈ પૂરી પાડવાનો હેતુ ધરાવે છે.\n લિંક: https://pmksy.gov.in/\n\n - **ગોબરધન (GOBARdhan) યોજના**: ગ્રામીણ વિસ્તારો માટે 'કચરામાંથી સંપત્તિ'ની પહેલ, જેમાં ઘન કચરા અને પશુઓના ગોબરને બાયોગેસ અને જૈવિક ખાતર જેવા ઉપયોગી સંસાધનોમાં રૂપાંતરિત કરવામાં આવે છે.\n લિંક: https://sbm.gov.in/gbdhn/index",
        'health_intro': "🏥 આરોગ્ય સલાહ અને યોજનાઓ",
        'health_content': "તમે આરોગ્ય સલાહ કેવી રીતે મેળવી શકો છો અને સરકારી આરોગ્ય યોજનાઓ વિશેની માહિતી અહીં આપેલી છે:\n\n - **eSanjeevani**: ભારત સરકારની એક રાષ્ટ્રીય ટેલિમેડિસિન સેવા જે મફત ઓનલાઇન ડોક્ટર સલાહ પૂરી પાડે છે.\n લિંક: https://esanjeevani.mohfw.gov.in/\n\n - **આયુષ્માન ભારત - પ્રધાન મંત્રી જન આરોગ્ય યોજના (PM-JAY)**: વિશ્વની સૌથી મોટી આરોગ્ય ખાતરી યોજના જે ગરીબ અને સંવેદનશીલ પરિવારો માટે પ્રતિ વર્ષ પ્રતિ પરિવાર ₹5 લાખનું આરોગ્ય કવર પૂરું પાડે છે.\n લિંક: https://nha.gov.in/PM-JAY",
        'sanitation_intro': "🚽 સ્વચ્છતા જાગૃતિ",
        'sanitation_content': "સમુદાયના આરોગ્ય માટે સ્વચ્છતા જાગૃતિ ખૂબ જ મહત્વપૂર્ણ છે. ભારત સરકારે સ્વચ્છતા અને સ્વચ્છતાને પ્રોત્સાહન આપવા માટે એક વિશાળ ઝુંબેશ શરૂ કરી છે.\n\n - **સ્વચ્છ ભારત મિશન (SBM)**: ખુલ્લામાં શૌચને નાબૂદ કરવા અને ઘન કચરા વ્યવસ્થાપનમાં સુધારો કરવા માટેનો દેશવ્યાપી કાર્યક્રમ. તે ગ્રામીણ અને શહેરી બંને વિસ્તારોમાં શૌચાલય બનાવવા માટે નાણાકીય સહાય પૂરી પાડે છે.\n લિંક: https://swachhbharatmission.gov.in/\n\n - **રાષ્ટ્રીય આરોગ્ય મિશન (NHM) ની ભૂમિકા**: NHM આરોગ્ય પરિણામો સુધારવા પર ધ્યાન કેન્દ્રિત કરે છે, જે સીધા સ્વચ્છતા અને સ્વચ્છતા સાથે જોડાયેલા છે. તે રોગોને અટકાવવા માટે સ્વસ્થ સ્વચ્છતા પ્રથાઓ વિશે જાગૃતિ લાવવાનું કામ કરે છે.",
        'skills_intro': "🎓 કૌશલ્યો અને શિક્ષણ",
        'skills_content': "વ્યક્તિગત વિકાસ અને રાષ્ટ્રીય પ્રગતિ માટે કૌશલ્ય વિકાસ અને શિક્ષણ આવશ્યક છે. અહીં કેટલીક મુખ્ય સરકારી પહેલ આપેલી છે:\n\n - **પ્રધાન મંત્રી કૌશલ વિકાસ યોજના (PMKVY)**: ભારતીય યુવાનોની મોટી સંખ્યાને ઉદ્યોગ-સંબંધિત કૌશલ્ય તાલીમ લેવા સક્ષમ બનાવવાની મુખ્ય યોજના જેથી તેઓ વધુ સારી આજીવિકા સુરક્ષિત કરી શકે.\n લિંક: https://pmkvyofficial.org/\n\n - **રાષ્ટ્રીય શિક્ષણ નીતિ (NEP) 2020**: ભારતની શિક્ષણ પ્રણાલીને રૂપાંતરિત કરવાના ઉદ્દેશ્ય સાથેની એક વ્યાપક નીતિ. તે નાની ઉંમરથી જ વ્યવસાયિક અને કૌશલ્ય-આધારિત શિક્ષણને મુખ્ય પ્રવાહના અભ્યાસક્રમમાં એકીકૃત કરે છે.\n લિંક: https://www.education.gov.in/nep",
        'digital_india_intro': "🇮🇳 ડિજિટલ ઇન્ડિયા",
        'digital_india_content': "ડિજિટલ ઇન્ડિયા કાર્યક્રમનો ઉદ્દેશ ભારતને ડિજિટલ રીતે સશક્ત સમાજ અને જ્ઞાન અર્થતંત્રમાં રૂપાંતરિત કરવાનો છે. મુખ્ય પહેલોમાં શામેલ છે:\n\n - **ડિજી લોકર (DigiLocker)**: નાગરિકોને તેમના સત્તાવાર દસ્તાવેજોને સુરક્ષિત રીતે સંગ્રહિત કરવા અને ઍક્સેસ કરવા માટે એક ડિજિટલ જગ્યા પૂરી પાડે છે.\n - **ભારતનેટ (BharatNet)**: તમામ ગ્રામ પંચાયતોને હાઇ-સ્પીડ ઇન્ટરનેટ કનેક્ટિવિટી પૂરી પાડવાનો હેતુ ધરાવે છે.",
        'make_in_india_intro': "🇮🇳 મેક ઇન ઇન્ડિયા",
        'make_in_india_content': "'મેક ઇન ઇન્ડિયા' પહેલ કંપનીઓને ભારતમાં તેમના ઉત્પાદનોનું ઉત્પાદન કરવા માટે પ્રોત્સાહિત કરે છે. તેનો ઉદ્દેશ આર્થિક વિકાસને વેગ આપવા, નોકરીઓનું સર્જન કરવા અને વિદેશી રોકાણ આકર્ષવાનો છે.",
        'emergency_intro': "🚨 કટોકટી અને હેલ્પલાઇન સપોર્ટ",
        'emergency_content': "કટોકટીના કિસ્સામાં, તમે આ હેલ્પલાઇન નંબરોનો ઉપયોગ કરી શકો છો:\n\n - **ઓલ-ઇન-વન કટોકટી નંબર**: **112** (પોલીસ, ફાયર, એમ્બ્યુલન્સ)\n - **પોલીસ**: **100**\n - **ફાયર**: **101**\n - **એમ્બ્યુલન્સ**: **108**\n - **આપત્તિ વ્યવસ્થાપન**: **1078**\n - **મહિલા હેલ્પલાઇન**: **1091**\n - **કિસાન કોલ સેન્ટર (ખેડૂતો માટે)**: **1800-180-1551**",
        'creator': "આ ચેટબોટ ગ્રુપ 7 દ્વારા બનાવવામાં આવ્યો છે.",
        'help_text': "અહીં ઉપલબ્ધ આદેશો છે:\n- 'info': ડિજિટલ સાક્ષરતા વિશે જાણો.\n- 'security': ઓનલાઈન સુરક્ષા ટિપ્સ મેળવો.\n- 'quiz': તમારા જ્ઞાનને ચકાસો.\n- 'agri': કૃષિ યોજનાઓ પર માહિતી.\n- 'health': આરોગ્ય યોજનાઓ પર માહિતી.\n- 'skills': શિક્ષણ પહેલ પર માહિતી.\n- 'sanitation': સ્વચ્છતા વિશે જાણો.\n- 'emergency': હેલ્પલાઇન નંબરો મેળવો.\n- 'digital_india': પહેલ વિશે.\n- 'make_in_india': પહેલ વિશે.\n- 'joke': એક જોક મેળવો.\n- 'image': એક છબી બનાવો (સિમ્યુલેશન).\n- 'time': વર્તમાન સમય મેળવો.\n- 'date': આજની તારીખ મેળવો.\n- 'weather': લખનઉમાં હવામાન જાણો.\n- 'creator': જુઓ કે આ ચેટબોટ કોણે બનાવ્યો.",
        'log_message': "વપરાશકર્તાનો પ્રશ્ન લોગ થયો."
    },
    'bn': {
        'title': "ডিজিটাল লিটারেসি চ্যাটবট",
        'lang_select_prompt': "চ্যাটবটের জন্য একটি ভাষা নির্বাচন করুন:",
        'lang_desc': "বাংলা (Bengali)",
        'welcome': "নমস্কার! আমি আপনার ডিজিটাল লিটারেসি চ্যাটবট, গ্রুপ 7 দ্বারা নির্মিত। আমি আপনাকে অনলাইন সুরক্ষা এবং দক্ষতা সম্পর্কে জানতে সাহায্য করতে পারি। সমস্ত উপলব্ধ কমান্ড দেখতে 'help' টাইপ করুন।",
        'info_intro': "🌐 ডিজিটাল লিটারেসি কী?",
        'info_content': "ডিজিটাল লিটারেসি হল কম্পিউটার, মোবাইল ফোন এবং ইন্টারনেটের মতো ডিজিটাল ডিভাইসগুলি সঠিকভাবে ব্যবহার করার ক্ষমতা। এটি আমাদের অনলাইন পরিষেবা, ব্যাংকিং, শিক্ষা এবং যোগাযোগে সহায়তা করে।\n\nউদাহরণ:\n - অনলাইন ব্যাংকিং ব্যবহার করা\n - ইমেল পাঠানো\n - শক্তিশালী পাসওয়ার্ড তৈরি করা\n - সাইবার নিরাপত্তা নিয়মাবলী অনুসরণ করা",
        'security_tips': "🔒 অনলাইন নিরাপত্তা টিপস",
        'security_content': "অনলাইন নিরাপত্তার জন্য সাইবার নিরাপত্তা অত্যন্ত গুরুত্বপূর্ণ।\n1. **ওটিপি সতর্কতা**: আপনার ওয়ান-টাইম পাসওয়ার্ড (ওটিপি) কখনও কারও সাথে শেয়ার করবেন না, এমনকি ব্যাংক কর্মচারীদের সাথেও নয়। ওটিপি শুধুমাত্র আপনার ব্যবহারের জন্য।\n2. **ফিশিং**: ব্যক্তিগত তথ্য চাওয়া সন্দেহজনক ইমেল বা বার্তা থেকে সতর্ক থাকুন।\n3. **শক্তিশালী পাসওয়ার্ড**: অক্ষর, সংখ্যা এবং বিশেষ অক্ষরের মিশ্রণ ব্যবহার করুন।\n4. **পাবলিক ওয়াই-ফাই**: পাবলিক ওয়াই-ফাই নেটওয়ার্কে সংবেদনশীল লেনদেন (যেমন ব্যাংকিং) এড়িয়ে চলুন।",
        'quiz_intro': "📝 আসুন একটি ছোট কুইজ করি:\n",
        'q1': "1️⃣ প্রশ্ন: একটি শক্তিশালী পাসওয়ার্ডে কী থাকা উচিত?",
        'q1_options': "a) শুধু নাম\nb) অক্ষর, সংখ্যা এবং বিশেষ অক্ষরের মিশ্রণ\nc) জন্ম তারিখ",
        'q1_ans': 'b',
        'q2': "2️⃣ প্রশ্ন: একজন অজানা ব্যক্তির পাঠানো লিঙ্কের সাথে আপনার কী করা উচিত?",
        'q2_options': "a) সঙ্গে সঙ্গে ক্লিক করুন\nb) উপেক্ষা করুন\nc) সবার সাথে শেয়ার করুন",
        'q2_ans': 'b',
        'q3': "3️⃣ প্রশ্ন: আপনার কি ওটিপি ব্যাংক প্রতিনিধির সাথে শেয়ার করা উচিত?",
        'q3_options': "a) হ্যাঁ\nb) না, কখনওই না\nc) শুধুমাত্র যদি তারা আপনাকে ব্যাংক নম্বর থেকে ফোন করে",
        'q3_ans': 'b',
        'q4': "4️⃣ প্রশ্ন: ফিশিং কী?",
        'q4_options': "a) পুকুরে মাছ ধরা\nb) জাল ইমেল ব্যবহার করে ব্যক্তিগত তথ্য চুরির চেষ্টা\nc) এক ধরনের অনলাইন গেম",
        'q4_ans': 'b',
        'q5': "5️⃣ প্রশ্ন: পাবলিক ওয়াই-ফাইতে অনলাইন ব্যাংকিং করা কি নিরাপদ?",
        'q5_options': "a) হ্যাঁ\nb) না, এটি ঝুঁকিপূর্ণ\nc) শুধুমাত্র যদি ওয়াই-ফাই বিনামূল্যে হয়",
        'q5_ans': 'b',
        'correct': "সঠিক! ✅",
        'incorrect': "ভুল। ❌ সঠিক উত্তর হল: ",
        'your_score': "🎉 আপনার চূড়ান্ত স্কোর: ",
        'quiz_end_excellent': "দারুণ! আপনি একজন ডিজিটাল লিটারেসি বিশেষজ্ঞ।",
        'quiz_end_good': "আপনি সঠিক পথে আছেন! আর একটু অনুশীলন আপনাকে বিশেষজ্ঞ করে তুলবে।",
        'quiz_end_average': "শিখতে থাকুন! অনুশীলনই সাফল্যের চাবিকাঠি।",
        'nlp_positive': "আপনার প্রতিক্রিয়ার জন্য অনেক ধন্যবাদ! 😊",
        'nlp_negative': "শুনে খারাপ লাগল। আমি আপনাকে আরও ভালোভাবে কীভাবে সাহায্য করতে পারি? 🤔",
        'nlp_neutral': "ঠিক আছে, আমি বুঝতে পেরেছি। আপনার কোন প্রশ্ন থাকলে জিজ্ঞাসা করতে পারেন। 🧐",
        'unknown_command': "দুঃখিত, আমি এটি বুঝতে পারিনি। উপলব্ধ কমান্ডগুলির তালিকা দেখতে 'help' টাইপ করুন।",
        'otp_warning': "🚫 নিরাপত্তা সতর্কতা: মনে হচ্ছে আপনি ওটিপি উল্লেখ করেছেন। মনে রাখবেন, আপনার ওয়ান-টাইম পাসওয়ার্ড কারও সাথে শেয়ার করবেন না। অনলাইনে নিরাপদে থাকুন!",
        'time': "এখন সময়: ",
        'date': "আজকের তারিখ: ",
        'weather': "লখনউতে বর্তমান আবহাওয়া: {weather_desc}",
        'image_prompt': "আপনি যে ছবিটি তৈরি করতে চান তার বর্ণনা দিন।",
        'image_generating': "🎨 আপনার ছবি তৈরি করা হচ্ছে: '{prompt}'। এতে কিছুক্ষণ সময় লাগতে পারে...",
        'image_link': "🖼️ আপনার ছবি তৈরি! এখানে দেখুন: ",
        'joke_intro': "😂 আপনার জন্য একটি জোক:",
        'jokes': [
            "শিক্ষক: তোমরা সবাই এমন একটা কাজ এর নাম বল যা তোমরা চোখ বন্ধ করে করতে পার। ছাত্র: छींक দেওয়া স্যার!",
            "রোগী: ডাক্তার সাহেব, আমার সবকিছু দুটো করে দেখার রোগ হয়েছে। ডাক্তার: আরে! আমার চেম্বারে তো একটাই চেয়ার আছে, আপনারা দুজন বসলেন কোথায়?"
        ],
        'agri_intro': "🌾 কৃষি এবং সরকারি প্রকল্প",
        'agri_content': "কৃষি হল উদ্ভিদ ও পশুপালনের বিজ্ঞান এবং অনুশীলন। এখানে কিছু প্রধান সরকারি প্রকল্প রয়েছে যা কৃষকদের সাহায্য করে:\n\n - **প্রধানমন্ত্রী কিষাণ সম্মান নিধি (PM-KISAN)**: কৃষকদের জন্য একটি আয় সহায়তা প্রকল্প।\n লিঙ্ক: https://pmkisan.gov.in/\n\n - **প্রধানমন্ত্রী ফসল বিমা যোজনা (PMFBY)**: কৃষকদের ক্ষতি থেকে রক্ষা করার জন্য একটি ফসল বিমা প্রকল্প।\n লিঙ্ক: https://pmfby.gov.in/\n\n - **কিষাণ ক্রেডিট কার্ড (KCC)**: কৃষকদের সময়মতো ঋণ প্রদানের একটি প্রকল্প।\n লিঙ্ক: https://www.india.gov.in/schemes-kisan-credit-card-scheme",
        'health_intro': "🏥 স্বাস্থ্য পরামর্শ এবং প্রকল্প",
        'health_content': "আপনি কীভাবে স্বাস্থ্য পরামর্শ এবং সরকারি স্বাস্থ্য প্রকল্প সম্পর্কে তথ্য পেতে পারেন তা এখানে দেওয়া হল:\n\n - **eSanjeevani**: ভারত সরকারের একটি জাতীয় টেলিমেডিসিন পরিষেবা যা বিনামূল্যে অনলাইন ডাক্তার পরামর্শ প্রদান করে।\n লিঙ্ক: https://esanjeevani.mohfw.gov.in/\n\n - **আয়ুষ্মান ভারত - প্রধানমন্ত্রী জন আরোগ্য যোজনা (PM-JAY)**: বিশ্বের বৃহত্তম স্বাস্থ্য নিশ্চয়তা প্রকল্প যা দরিদ্র এবং দুর্বল পরিবারগুলির জন্য প্রতি বছর পরিবার প্রতি ₹5 লক্ষের স্বাস্থ্য কভার প্রদান করে।\n লিঙ্ক: https://nha.gov.in/PM-JAY",
        'sanitation_intro': "🚽 স্যানিটেশন সচেতনতা",
        'sanitation_content': "সম্প্রদায়ের স্বাস্থ্যের জন্য স্যানিটেশন সচেতনতা অত্যন্ত গুরুত্বপূর্ণ। ভারত সরকার পরিচ্ছন্নতা প্রচারের জন্য একটি বিশাল অভিযান শুরু করেছে।\n\n - **স্বচ্ছ ভারত মিশন (SBM)**: খোলা স্থানে মলত্যাগ নির্মূল এবং কঠিন বর্জ্য ব্যবস্থাপনার উন্নতির জন্য একটি দেশব্যাপী অভিযান।\n লিঙ্ক: https://swachhbharatmission.gov.in/",
        'skills_intro': "🎓 দক্ষতা এবং শিক্ষা",
        'skills_content': "ব্যক্তিগত বৃদ্ধি এবং জাতীয় অগ্রগতির জন্য দক্ষতা উন্নয়ন এবং শিক্ষা অপরিহার্য। এখানে কিছু প্রধান সরকারি উদ্যোগ রয়েছে:\n\n - **প্রধানমন্ত্রী কৌশল বিকাশ যোজনা (PMKVY)**: ভারতীয় যুবকদের একটি বড় অংশকে শিল্প-প্রাসঙ্গিক দক্ষতা প্রশিক্ষণে সক্ষম করার জন্য ফ্ল্যাগশিপ প্রকল্প।\n লিঙ্ক: https://pmkvyofficial.org/\n\n - **জাতীয় শিক্ষা নীতি (NEP) 2020**: ভারতের শিক্ষা ব্যবস্থাকে রূপান্তরিত করার লক্ষ্যে একটি ব্যাপক নীতি।\n লিঙ্ক: https://www.education.gov.in/nep",
        'digital_india_intro': "🇮🇳 ডিজিটাল ইন্ডিয়া",
        'digital_india_content': "ডিজিটাল ইন্ডিয়া প্রোগ্রামের লক্ষ্য ভারতকে একটি ডিজিটালভাবে ক্ষমতায়িত সমাজ এবং জ্ঞান অর্থনীতিতে রূপান্তরিত করা।\n\n - **ডিজি-লকার (DigiLocker)**: নাগরিকদের তাদের অফিসিয়াল নথিগুলি সুরক্ষিতভাবে সংরক্ষণ এবং অ্যাক্সেস করার জন্য একটি ডিজিটাল স্থান সরবরাহ করে।\n - **ভারতনেট (BharatNet)**: সমস্ত গ্রাম পঞ্চায়েতকে উচ্চ-গতির ইন্টারনেট সংযোগ প্রদানের লক্ষ্য রাখে।",
        'make_in_india_intro': "🇮🇳 মেক ইন ইন্ডিয়া",
        'make_in_india_content': "'মেক ইন ইন্ডিয়া' উদ্যোগটি সংস্থাগুলিকে ভারতে তাদের পণ্য তৈরি করতে উৎসাহিত করে। এর লক্ষ্য অর্থনৈতিক প্রবৃদ্ধি বাড়ানো, চাকরি তৈরি করা এবং বিদেশী বিনিয়োগ আকর্ষণ করা।",
        'emergency_intro': "🚨 জরুরি এবং হেল্পলাইন সহায়তা",
        'emergency_content': "জরুরি অবস্থায়, আপনি এই হেল্পলাইন নম্বরগুলি ব্যবহার করতে পারেন:\n\n - **অল-ইন-ওয়ান জরুরি নম্বর**: **112**\n - **পুলিশ**: **100**\n - **ফায়ার**: **101**\n - **অ্যাম্বুলেন্স**: **108**\n - **মহিলা হেল্পলাইন**: **1091**\n - **কিষাণ কল সেন্টার**: **1800-180-1551**",
        'creator': "এই চ্যাটবটটি গ্রুপ 7 দ্বারা নির্মিত।",
        'help_text': "উপলব্ধ কমান্ডগুলি এখানে:\n- 'info': ডিজিটাল লিটারেসি সম্পর্কে জানুন।\n- 'security': অনলাইন নিরাপত্তা টিপস পান।\n- 'quiz': আপনার জ্ঞান পরীক্ষা করুন।\n- 'agri', 'health', 'skills', 'sanitation': বিভিন্ন সরকারি প্রকল্প সম্পর্কে জানুন।\n- 'emergency': হেল্পলাইন নম্বর পান।\n- 'joke': একটি জোক শুনুন।\n- 'time', 'date', 'weather': সময়, তারিখ এবং আবহাওয়া জানুন।\n- 'creator': দেখুন কে এই চ্যাটবটটি তৈরি করেছে।",
        'log_message': "ব্যবহারকারীর প্রশ্ন লগ করা হয়েছে।"
    },
    'ta': {
        'title': "டிஜிட்டல் எழுத்தறிவு அரட்டைப்பெட்டி",
        'lang_select_prompt': "அரட்டைப்பெட்டிக்கான மொழியைத் தேர்ந்தெடுக்கவும்:",
        'lang_desc': "தமிழ் (Tamil)",
        'welcome': "வணக்கம்! நான் உங்கள் டிஜிட்டல் எழுத்தறிவு அரட்டைப்பெட்டி, குழு 7 உருவாக்கியது. ஆன்லைன் பாதுகாப்பு மற்றும் திறன்களைப் பற்றி அறிய நான் உங்களுக்கு உதவ முடியும். கிடைக்கக்கூடிய அனைத்து கட்டளைகளையும் காண 'help' என தட்டச்சு செய்யவும்.",
        'info_intro': "🌐 டிஜிட்டல் எழுத்தறிவு என்றால் என்ன?",
        'info_content': "டிஜிட்டல் எழுத்தறிவு என்பது கணினிகள், மொபைல் போன்கள் மற்றும் இணையம் போன்ற டிஜிட்டல் சாதனங்களை சரியாகப் பயன்படுத்தும் திறன். இது ஆன்லைன் சேவைகள், வங்கி, கல்வி மற்றும் தகவல்தொடர்புகளில் நமக்கு உதவுகிறது.\n\nஎடுத்துக்காட்டுகள்:\n - ஆன்லைன் வங்கியைப் பயன்படுத்துதல்\n - மின்னஞ்சல்களை அனுப்புதல்\n - வலுவான கடவுச்சொற்களை உருவாக்குதல்\n - சைபர் பாதுகாப்பு விதிகளைப் பின்பற்றுதல்",
        'security_tips': "🔒 ஆன்லைன் பாதுகாப்பு குறிப்புகள்",
        'security_content': "ஆன்லைன் பாதுகாப்பிற்கு சைபர் பாதுகாப்பு முக்கியமானது.\n1. **OTP எச்சரிக்கை**: உங்கள் ஒருமுறை கடவுச்சொல்லை (OTP) யாருடனும் பகிர வேண்டாம், வங்கி ஊழியர்களுடன் கூட. OTP உங்கள் பயன்பாட்டிற்கு மட்டுமே.\n2. **ஃபிஷிங் (Phishing)**: தனிப்பட்ட தகவல்களைக் கேட்கும் சந்தேகத்திற்கிடமான மின்னஞ்சல்கள் அல்லது செய்திகளிடம் கவனமாக இருங்கள்.\n3. **வலுவான கடவுச்சொற்கள்**: எழுத்துக்கள், எண்கள் மற்றும் சிறப்பு குறியீடுகளின் கலவையைப் பயன்படுத்தவும்.\n4. **பொது Wi-Fi**: பொது Wi-Fi நெட்வொர்க்குகளில் முக்கியமான பரிவர்த்தனைகளை (வங்கி போன்றவை) தவிர்க்கவும்.",
        'quiz_intro': "📝 ஒரு சிறிய வினாடி வினா செய்வோம்:\n",
        'q1': "1️⃣ கேள்வி: ஒரு வலுவான கடவுச்சொல்லில் என்ன இருக்க வேண்டும்?",
        'q1_options': "a) பெயர்கள் மட்டும்\nb) எழுத்துக்கள், எண்கள் மற்றும் சிறப்பு குறியீடுகளின் கலவை\nc) பிறந்த தேதி",
        'q1_ans': 'b',
        'q2': "2️⃣ கேள்வி: தெரியாத நபர் அனுப்பிய இணைப்பை என்ன செய்ய வேண்டும்?",
        'q2_options': "a) உடனடியாக கிளிக் செய்யவும்\nb) புறக்கணிக்கவும்\nc) எல்லோருடனும் பகிரவும்",
        'q2_ans': 'b',
        'q3': "3️⃣ கேள்வி: உங்கள் OTP-ஐ வங்கி பிரதிநிதியுடன் பகிர வேண்டுமா?",
        'q3_options': "a) ஆம்\nb) இல்லை, ஒருபோதும் கூடாது\nc) அவர்கள் வங்கி எண்ணிலிருந்து அழைத்தால் மட்டுமே",
        'q3_ans': 'b',
        'q4': "4️⃣ கேள்வி: ஃபிஷிங் (Phishing) என்றால் என்ன?",
        'q4_options': "a) குளத்தில் மீன்பிடித்தல்\nb) போலி மின்னஞ்சல்களைப் பயன்படுத்தி தனிப்பட்ட தகவல்களைத் திருட முயற்சித்தல்\nc) ஒரு வகை ஆன்லைன் விளையாட்டு",
        'q4_ans': 'b',
        'q5': "5️⃣ கேள்வி: பொது Wi-Fi-ல் ஆன்லைன் வங்கி செய்வது பாதுகாப்பானதா?",
        'q5_options': "a) ஆம்\nb) இல்லை, அது ஆபத்தானது\nc) Wi-Fi இலவசமாக இருந்தால் மட்டுமே",
        'q5_ans': 'b',
        'correct': "சரி! ✅",
        'incorrect': "தவறு. ❌ சரியான பதில்: ",
        'your_score': "🎉 உங்கள் இறுதி மதிப்பெண்: ",
        'quiz_end_excellent': "சிறந்த வேலை! நீங்கள் ஒரு டிஜிட்டல் எழுத்தறிவு நிபுணர்.",
        'quiz_end_good': "நீங்கள் சரியான பாதையில் இருக்கிறீர்கள்! இன்னும் கொஞ்சம் பயிற்சி உங்களை ஒரு நிபுணராக்கும்.",
        'quiz_end_average': "தொடர்ந்து கற்றுக்கொள்ளுங்கள்! பயிற்சி சரியானதாக்கும்.",
        'nlp_positive': "உங்கள் கருத்து பாராட்டத்தக்கது! நேர்மறையான வார்த்தைகளுக்கு நன்றி. 😊",
        'nlp_negative': "அதைக் கேட்பதற்கு வருந்துகிறேன். நான் உங்களுக்கு எப்படி சிறப்பாக உதவ முடியும்? 🤔",
        'nlp_neutral': "சரி, நான் புரிந்துகொள்கிறேன். உங்களுக்கு ஏதேனும் கேள்விகள் இருந்தால், தயங்காமல் கேட்கவும். 🧐",
        'unknown_command': "மன்னிக்கவும், எனக்கு அது புரியவில்லை. கிடைக்கக்கூடிய கட்டளைகளின் பட்டியலைக் காண 'help' என தட்டச்சு செய்யவும்.",
        'otp_warning': "🚫 பாதுகாப்பு எச்சரிக்கை: நீங்கள் OTP-ஐக் குறிப்பிட்டுள்ளதாகத் தெரிகிறது. உங்கள் ஒருமுறை கடவுச்சொல்லை யாருடனும் பகிர வேண்டாம். ஆன்லைனில் பாதுகாப்பாக இருங்கள்!",
        'time': "தற்போதைய நேரம்: ",
        'date': "இன்றைய தேதி: ",
        'weather': "லக்னோவில் தற்போதைய வானிலை: {weather_desc}",
        'image_prompt': "நீங்கள் உருவாக்க விரும்பும் படத்தின் விளக்கத்தைக் கொடுக்கவும்.",
        'image_generating': "🎨 உங்கள் படம் உருவாக்கப்படுகிறது: '{prompt}'. இதற்கு சிறிது நேரம் ஆகலாம்...",
        'image_link': "🖼️ உங்கள் படம் தயாராக உள்ளது! இங்கே பார்க்கவும்: ",
        'joke_intro': "😂 உங்களுக்காக ஒரு நகைச்சுவை:",
        'jokes': [
            "ஆசிரியர்: ஏன்டா நேத்து ஸ்கூலுக்கு வரல? மாணவன்: எங்க வீட்டுல பாட்டிக்கு உடம்பு சரியில்ல சார். ஆசிரியர்: ஓ அப்படியா, சரி போன வாரம் ஏன் வரல? மாணவன்: அப்போ எங்க பாட்டிக்கு உடம்பு நல்லா இருந்துச்சு சார்!",
            "நோயாளி: டாக்டர், எனக்கு படுத்தா தூக்கம் வரமாட்டேங்குது. டாக்டர்: அப்போ நின்னுக்கிட்டே தூங்குங்க."
        ],
        'agri_intro': "🌾 விவசாயம் மற்றும் அரசாங்க திட்டங்கள்",
        'agri_content': "விவசாயம் என்பது தாவரங்கள் மற்றும் கால்நடைகளை பயிரிடும் அறிவியல் மற்றும் நடைமுறை. விவசாயிகளுக்கு உதவும் சில முக்கிய அரசாங்க திட்டங்கள் இங்கே:\n\n - **பிரதம மந்திரி கிசான் சம்மான் நிதி (PM-KISAN)**: விவசாயிகளுக்கான வருமான ஆதரவு திட்டம்.\n இணைப்பு: https://pmkisan.gov.in/\n\n - **பிரதம மந்திரி ஃபசல் பீமா யோஜனா (PMFBY)**: விவசாயிகளை இழப்புகளிலிருந்து பாதுகாக்க ஒரு பயிர் காப்பீட்டுத் திட்டம்.\n இணைப்பு: https://pmfby.gov.in/",
        'health_intro': "🏥 சுகாதார ஆலோசனை மற்றும் திட்டங்கள்",
        'health_content': "சுகாதார ஆலோசனைகள் மற்றும் அரசாங்க சுகாதார திட்டங்கள் பற்றிய தகவல்களை இங்கே பெறலாம்:\n\n - **eSanjeevani**: இந்திய அரசின் ஒரு தேசிய தொலை மருத்துவ சேவை, இது இலவச ஆன்லைன் மருத்துவர் ஆலோசனைகளை வழங்குகிறது.\n இணைப்பு: https://esanjeevani.mohfw.gov.in/\n\n - **ஆயுஷ்மான் பாரத் - பிரதம மந்திரி ஜன் ஆரோக்கிய யோஜனா (PM-JAY)**: ஏழை மற்றும் பாதிக்கப்படக்கூடிய குடும்பங்களுக்கு ஆண்டுக்கு ஒரு குடும்பத்திற்கு ₹5 லட்சம் சுகாதாரப் பாதுகாப்பை வழங்கும் உலகின் மிகப்பெரிய சுகாதார உறுதி திட்டம்.\n இணைப்பு: https://nha.gov.in/PM-JAY",
        'sanitation_intro': "🚽 துப்புரவு விழிப்புணர்வு",
        'sanitation_content': "சமூக சுகாதாரத்திற்கு துப்புரவு விழிப்புணர்வு முக்கியமானது. இந்திய அரசு தூய்மையை ஊக்குவிக்க ஒரு பெரிய பிரச்சாரத்தை தொடங்கியுள்ளது.\n\n - **ஸ்வச் பாரத் மிஷன் (SBM)**: திறந்தவெளியில் மலம் கழிப்பதை ஒழிக்கவும், திடக்கழிவு ব্যবস্থাপையை மேம்படுத்தவும் ஒரு நாடு தழுவிய பிரச்சாரம்.\n இணைப்பு: https://swachhbharatmission.gov.in/",
        'skills_intro': "🎓 திறன்கள் மற்றும் கல்வி",
        'skills_content': "தனிப்பட்ட வளர்ச்சிக்கும் நாட்டின் முன்னேற்றத்திற்கும் திறன் மேம்பாடு மற்றும் கல்வி அவசியம். இங்கே சில முக்கிய அரசாங்க முயற்சிகள் உள்ளன:\n\n - **பிரதம மந்திரி கௌஷல் விகாஸ் யோஜனா (PMKVY)**: இந்திய இளைஞர்கள் தொழில்-தொடர்புடைய திறன் பயிற்சியை மேற்கொள்ள உதவும் முதன்மைத் திட்டம்.\n இணைப்பு: https://pmkvyofficial.org/\n\n - **தேசிய கல்விக் கொள்கை (NEP) 2020**: இந்தியாவின் கல்வி முறையை மாற்றுவதை நோக்கமாகக் கொண்ட ஒரு விரிவான கொள்கை.\n இணைப்பு: https://www.education.gov.in/nep",
        'digital_india_intro': "🇮🇳 டிஜிட்டல் இந்தியா",
        'digital_india_content': "டிஜிட்டல் இந்தியா திட்டத்தின் நோக்கம் இந்தியாவை டிஜிட்டல் அதிகாரம் பெற்ற சமூகமாகவும் அறிவுப் பொருளாதாரமாகவும் மாற்றுவதாகும்.\n\n - **டிஜி-லாக்கர் (DigiLocker)**: குடிமக்கள் தங்கள் அதிகாரப்பூர்வ ஆவணங்களைப் பாதுகாப்பாக சேமிக்கவும் அணுகவும் ஒரு டிஜிட்டல் இடத்தை வழங்குகிறது.\n - **பாரத்நெட் (BharatNet)**: அனைத்து கிராம பஞ்சாயத்துகளுக்கும் அதிவேக இணைய இணைப்பை வழங்குவதை நோக்கமாகக் கொண்டுள்ளது.",
        'make_in_india_intro': "🇮🇳 மேக் இன் இந்தியா",
        'make_in_india_content': "'மேக் இன் இந்தியா' முயற்சி நிறுவனங்களை இந்தியாவில் தங்கள் தயாரிப்புகளை உற்பத்தி செய்ய ஊக்குவிக்கிறது. இதன் குறிக்கோள் பொருளாதார வளர்ச்சியை அதிகரிப்பது, வேலைவாய்ப்புகளை உருவாக்குவது மற்றும் வெளிநாட்டு முதலீட்டை ஈர்ப்பது.",
        'emergency_intro': "🚨 அவசர மற்றும் உதவி எண்கள்",
        'emergency_content': "அவசர காலத்தில், இந்த உதவி எண்களைப் பயன்படுத்தலாம்:\n\n - **அனைத்து அவசர எண்**: **112**\n - **காவல்துறை**: **100**\n - **தீயணைப்பு**: **101**\n - **ஆம்புலன்ஸ்**: **108**\n - **பெண்கள் உதவி எண்**: **1091**\n - **விவசாயிகள் அழைப்பு மையம்**: **1800-180-1551**",
        'creator': "இந்த அரட்டைப்பெட்டி குழு 7 ஆல் உருவாக்கப்பட்டது.",
        'help_text': "கிடைக்கக்கூடிய கட்டளைகள் இங்கே:\n- 'info': டிஜிட்டல் எழுத்தறிவு பற்றி அறியவும்.\n- 'security': ஆன்லைன் பாதுகாப்பு குறிப்புகளைப் பெறவும்.\n- 'quiz': உங்கள் அறிவை சோதிக்கவும்.\n- 'agri', 'health', 'skills', 'sanitation': பல்வேறு அரசாங்க திட்டங்களைப் பற்றி அறியவும்.\n- 'emergency': உதவி எண்களைப் பெறவும்.\n- 'joke': ஒரு நகைச்சுவையைப் பெறவும்.\n- 'time', 'date', 'weather': நேரம், தேதி மற்றும் வானிலை அறியவும்.\n- 'creator': இந்த அரட்டைப்பெட்டியை உருவாக்கியவர் யார் என்று பார்க்கவும்.",
        'log_message': "பயனர் கேள்வி பதிவு செய்யப்பட்டது."
    },
    'mr': {
        'title': "डिजिटल साक्षरता चॅटबॉट",
        'lang_select_prompt': "चॅटबॉटसाठी एक भाषा निवडा:",
        'lang_desc': "मराठी (Marathi)",
        'welcome': "नमस्कार! मी तुमचा डिजिटल साक्षरता चॅटबॉट आहे, जो ग्रुप 7 ने बनवला आहे. मी तुम्हाला ऑनलाइन सुरक्षा आणि कौशल्यांबद्दल शिकण्यास मदत करू शकेन. सर्व उपलब्ध कमांड पाहण्यासाठी 'help' टाइप करा.",
        'info_intro': "🌐 डिजिटल साक्षरता म्हणजे काय?",
        'info_content': "डिजिटल साक्षरता म्हणजे संगणक, मोबाईल फोन आणि इंटरनेट यांसारख्या डिजिटल उपकरणांचा योग्य वापर करण्याची क्षमता. हे आपल्याला ऑनलाइन सेवा, बँकिंग, शिक्षण आणि संवाद साधण्यात मदत करते.\n\nउदाहरणे:\n - ऑनलाइन बँकिंग वापरणे\n - ईमेल पाठवणे\n - मजबूत पासवर्ड तयार करणे\n - सायबर सुरक्षा नियमांचे पालन करणे",
        'security_tips': "🔒 ऑनलाइन सुरक्षा टिप्स",
        'security_content': "ऑनलाइन सुरक्षेसाठी सायबर सुरक्षा महत्त्वाची आहे.\n1. **ओटीपी चेतावणी**: तुमचा वन-टाइम पासवर्ड (ओटीपी) कधीही कोणासोबत शेअर करू नका, अगदी बँक कर्मचाऱ्यांसोबतही नाही. ओटीपी फक्त तुमच्या वापरासाठी आहे.\n2. **फिशिंग**: वैयक्तिक माहिती विचारणाऱ्या संशयास्पद ईमेल किंवा मेसेजपासून सावध रहा.\n3. **मजबूत पासवर्ड**: अक्षरे, अंक आणि विशेष चिन्हे यांचे मिश्रण वापरा.\n4. **सार्वजनिक वाय-फाय**: सार्वजनिक वाय-फाय नेटवर्कवर संवेदनशील व्यवहार (जसे की बँकिंग) करणे टाळा.",
        'quiz_intro': "📝 चला एक छोटी प्रश्नमंजुषा घेऊया:\n",
        'q1': "1️⃣ प्रश्न: मजबूत पासवर्डमध्ये काय असावे?",
        'q1_options': "a) फक्त नावे\nb) अक्षरे, अंक आणि विशेष चिन्हे यांचे मिश्रण\nc) जन्मतारीख",
        'q1_ans': 'b',
        'q2': "2️⃣ प्रश्न: अज्ञात व्यक्तीने पाठवलेल्या लिंकचे काय करावे?",
        'q2_options': "a) त्यावर लगेच क्लिक करा\nb) त्याकडे दुर्लक्ष करा\nc) ते सर्वांसोबत शेअर करा",
        'q2_ans': 'b',
        'q3': "3️⃣ प्रश्न: तुम्ही तुमचा ओटीपी बँक प्रतिनिधीसोबत शेअर करावा का?",
        'q3_options': "a) होय\nb) नाही, कधीच नाही\nc) फक्त जर त्यांनी तुम्हाला बँक नंबरवरून कॉल केला तर",
        'q3_ans': 'b',
        'q4': "4️⃣ प्रश्न: फिशिंग म्हणजे काय?",
        'q4_options': "a) तलावात मासेमारी करणे\nb) बनावट ईमेल वापरून वैयक्तिक माहिती चोरण्याचा प्रयत्न\nc) एक प्रकारचा ऑनलाइन गेम",
        'q4_ans': 'b',
        'q5': "5️⃣ प्रश्न: सार्वजनिक वाय-फायवर ऑनलाइन बँकिंग करणे सुरक्षित आहे का?",
        'q5_options': "a) होय\nb) नाही, ते धोकादायक आहे\nc) फक्त जर वाय-फाय मोफत असेल तर",
        'q5_ans': 'b',
        'correct': "बरोबर! ✅",
        'incorrect': "चूक. ❌ बरोबर उत्तर आहे: ",
        'your_score': "🎉 तुमचा अंतिम गुण: ",
        'quiz_end_excellent': "उत्तम! तुम्ही डिजिटल साक्षरतेचे तज्ञ आहात.",
        'quiz_end_good': "तुम्ही योग्य मार्गावर आहात! थोडा अधिक सराव तुम्हाला तज्ञ बनवेल.",
        'quiz_end_average': "शिकत रहा! सरावाने परिपूर्णता येते.",
        'nlp_positive': "तुमच्या प्रतिक्रियेबद्दल धन्यवाद! सकारात्मक शब्दांबद्दल आभारी आहे. 😊",
        'nlp_negative': "हे ऐकून वाईट वाटले. मी तुम्हाला अधिक चांगली मदत कशी करू शकेन? 🤔",
        'nlp_neutral': "ठीक आहे, मला समजले. तुमचे काही प्रश्न असल्यास, विचारायला संकोच करू नका. 🧐",
        'unknown_command': "माफ करा, मला ते समजले नाही. उपलब्ध कमांडची सूची पाहण्यासाठी 'help' टाइप करा.",
        'otp_warning': "🚫 सुरक्षा इशारा: असे दिसते की तुम्ही ओटीपीचा उल्लेख केला आहे. लक्षात ठेवा, तुमचा वन-टाइम पासवर्ड कोणासोबतही शेअर करू नका. ऑनलाइन सुरक्षित रहा!",
        'time': "सध्याची वेळ आहे: ",
        'date': "आजची तारीख आहे: ",
        'weather': "लखनऊमधील सध्याचे हवामान: {weather_desc}",
        'image_prompt': "कृपया तुम्हाला तयार करायच्या असलेल्या प्रतिमेचे वर्णन करा.",
        'image_generating': "🎨 तुमची प्रतिमा तयार होत आहे: '{prompt}'. याला थोडा वेळ लागू शकतो...",
        'image_link': "🖼️ तुमची प्रतिमा तयार आहे! येथे पहा: ",
        'joke_intro': "😂 तुमच्यासाठी एक विनोद:",
        'jokes': [
            "शिक्षक: मुलांनो, सांगा पाहू, ताजमहाल कोणी बांधला? बंड्या: मास्तर, गवंड्याने बांधला!",
            "गण्या: अरे, काल रात्री माझ्या घरात चोर शिरला होता. पिंट्या: मग? तू पोलिसांना बोलावलंस का? गण्या: नाही, तो अंधारात काहीतरी शोधत होता, मी पण त्याच्याबरोबर शोधायला लागलो."
        ],
        'agri_intro': "🌾 कृषी आणि सरकारी योजना",
        'agri_content': "कृषी म्हणजे वनस्पती आणि पशुधनाची लागवड करण्याचे शास्त्र आणि सराव. शेतकऱ्यांना मदत करणाऱ्या काही प्रमुख सरकारी योजना येथे आहेत:\n\n - **प्रधानमंत्री किसान सन्मान निधी (PM-KISAN)**: शेतकऱ्यांसाठी एक उत्पन्न समर्थन योजना.\n लिंक: https://pmkisan.gov.in/\n\n - **प्रधानमंत्री फसल विमा योजना (PMFBY)**: शेतकऱ्यांना नुकसानीपासून वाचवण्यासाठी एक पीक विमा योजना.\n लिंक: https://pmfby.gov.in/",
        'health_intro': "🏥 आरोग्य सल्ला आणि योजना",
        'health_content': "तुम्ही आरोग्य सल्ला आणि सरकारी आरोग्य योजनांबद्दल माहिती येथे मिळवू शकता:\n\n - **eSanjeevani**: भारत सरकारची एक राष्ट्रीय টেলিमेडिसिन सेवा जी मोफत ऑनलाइन डॉक्टर सल्ला देते.\n लिंक: https://esanjeevani.mohfw.gov.in/\n\n - **आयुष्मान भारत - प्रधानमंत्री जन आरोग्य योजना (PM-JAY)**: गरीब आणि गरजू कुटुंबांना दरवर्षी प्रति कुटुंब ₹5 लाखांचे आरोग्य कवच प्रदान करणारी जगातील सर्वात मोठी आरोग्य विमा योजना.\n लिंक: https://nha.gov.in/PM-JAY",
        'sanitation_intro': "🚽 स्वच्छता जागरूकता",
        'sanitation_content': "सामुदायिक आरोग्यासाठी स्वच्छता जागरूकता अत्यंत महत्त्वाची आहे. भारत सरकारने स्वच्छतेला प्रोत्साहन देण्यासाठी एक मोठी मोहीम सुरू केली आहे.\n\n - **स्वच्छ भारत मिशन (SBM)**: उघड्यावर शौचास जाणे बंद करणे आणि घनकचरा व्यवस्थापन सुधारण्यासाठी एक देशव्यापी मोहीम.\n लिंक: https://swachhbharatmission.gov.in/",
        'skills_intro': "🎓 कौशल्ये आणि शिक्षण",
        'skills_content': "वैयक्तिक वाढ आणि राष्ट्रीय प्रगतीसाठी कौशल्य विकास आणि शिक्षण आवश्यक आहे. येथे काही प्रमुख सरकारी उपक्रम आहेत:\n\n - **प्रधानमंत्री कौशल विकास योजना (PMKVY)**: मोठ्या संख्येने भारतीय तरुणांना उद्योगाशी संबंधित कौशल्य प्रशिक्षण घेण्यास सक्षम करणारी प्रमुख योजना.\n लिंक: https://pmkvyofficial.org/\n\n - **राष्ट्रीय शिक्षण धोरण (NEP) 2020**: भारताच्या शिक्षण प्रणालीत परिवर्तन घडवून आणण्याच्या उद्देशाने एक व्यापक धोरण.\n लिंक: https://www.education.gov.in/nep",
        'digital_india_intro': "🇮🇳 डिजिटल इंडिया",
        'digital_india_content': "डिजिटल इंडिया कार्यक्रमाचे उद्दिष्ट भारताला डिजिटल सक्षम समाज आणि ज्ञान अर्थव्यवस्थेत रूपांतरित करणे आहे.\n\n - **डिजी-लॉकर (DigiLocker)**: नागरिकांना त्यांची अधिकृत कागदपत्रे सुरक्षितपणे संग्रहित करण्यासाठी आणि त्यात प्रवेश करण्यासाठी एक डिजिटल जागा प्रदान करते.\n - **भारतनेट (BharatNet)**: सर्व ग्रामपंचायतींना हाय-स्पीड इंटरनेट कनेक्टिव्हिटी प्रदान करण्याचे उद्दिष्ट आहे.",
        'make_in_india_intro': "🇮🇳 मेक इन इंडिया",
        'make_in_india_content': "'मेक इन इंडिया' उपक्रम कंपन्यांना भारतात त्यांची उत्पादने तयार करण्यास प्रोत्साहित करतो. आर्थिक वाढीला चालना देणे, रोजगार निर्माण करणे आणि परदेशी गुंतवणूक आकर्षित करणे हे त्याचे उद्दिष्ट आहे.",
        'emergency_intro': "🚨 आपत्कालीन आणि हेल्पलाइन समर्थन",
        'emergency_content': "आपत्कालीन परिस्थितीत, तुम्ही हे हेल्पलाइन क्रमांक वापरू शकता:\n\n - **एकत्रित आपत्कालीन क्रमांक**: **112**\n - **पोलीस**: **100**\n - **अग्निशमन दल**: **101**\n - **रुग्णवाहिका**: **108**\n - **महिला हेल्पलाइन**: **1091**\n - **किसान कॉल सेंटर**: **1800-180-1551**",
        'creator': "हा चॅटबॉट ग्रुप 7 ने बनवला आहे.",
        'help_text': "येथे उपलब्ध कमांड आहेत:\n- 'info': डिजिटल साक्षरतेबद्दल जाणून घ्या.\n- 'security': ऑनलाइन सुरक्षा टिप्स मिळवा.\n- 'quiz': तुमच्या ज्ञानाची चाचणी घ्या.\n- 'agri', 'health', 'skills', 'sanitation': विविध सरकारी योजनांबद्दल जाणून घ्या.\n- 'emergency': हेल्पलाइन क्रमांक मिळवा.\n- 'joke': एक विनोद मिळवा.\n- 'time', 'date', 'weather': वेळ, तारीख आणि हवामान जाणून घ्या.\n- 'creator': हा चॅटबॉट कोणी बनवला ते पहा.",
        'log_message': "वापरकर्त्याचा प्रश्न लॉग केला गेला."
    }
}


class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Digital Literacy Chatbot")
        self.master.geometry("800x650")
        self.master.configure(bg="#E6E6FA")

        self.current_lang = 'en'
        self.state = "initial"
        self.quiz_score = 0
        self.quiz_question_num = 0

        self.main_frame = tk.Frame(self.master, bg="#E6E6FA")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.show_language_selection()

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_language_selection(self):
        self.clear_main_frame()
        self.state = "language_selection"
        self.master.title("Select Language")

        lang_label = tk.Label(self.main_frame, text="Please select a language:", font=("Helvetica", 16, "bold"), bg="#E6E6FA")
        lang_label.pack(pady=(50, 20))

        # Language selection buttons
        button_frame = tk.Frame(self.main_frame, bg="#E6E6FA")
        button_frame.pack(pady=20)

        row, col = 0, 0
        for lang_code, data in LANG_DATA.items():
            btn = tk.Button(button_frame, text=data['lang_desc'], font=("Helvetica", 14),
                            bg="#4682B4", fg="white", bd=0, padx=15, pady=8,
                            activebackground="#5F9EA0", activeforeground="white",
                            command=lambda code=lang_code: self.start_chat(code))
            btn.grid(row=row, column=col, padx=10, pady=10, sticky="ew")
            col += 1
            if col > 1: # 2 buttons per row
                col = 0
                row += 1

    def start_chat(self, lang_code):
        self.current_lang = lang_code
        self.master.title(LANG_DATA[self.current_lang]['title'])
        self.clear_main_frame()
        self.create_chat_widgets()
        self.display_message("Bot", LANG_DATA[self.current_lang]['welcome'])

    def create_chat_widgets(self):
        self.state = "initial"
        # --- Create Menu Bar ---
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Change Language", command=self.show_language_selection)
        file_menu.add_command(label="Clear Chat", command=self.clear_chat)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="Options", menu=file_menu)

        # --- Chat Display Area ---
        chat_font = font.Font(family="Helvetica", size=12)
        self.chat_display = scrolledtext.ScrolledText(self.main_frame, wrap=tk.WORD, bg="#F0F8FF", fg="#333333", font=chat_font, bd=0, padx=10, pady=10)
        self.chat_display.pack(padx=20, pady=(10, 10), fill=tk.BOTH, expand=True)
        self.chat_display.config(state=tk.DISABLED)

        # Configure tags for sender colors and hyperlinks
        self.chat_display.tag_config('user', foreground='#000080', font=("Helvetica", 12, "bold")) # Dark Blue
        self.chat_display.tag_config('bot', foreground='#006400', font=("Helvetica", 12, "bold")) # Dark Green
        self.chat_display.tag_config('hyperlink', foreground='blue', underline=1)
        self.chat_display.tag_bind('hyperlink', '<Enter>', self._show_hand_cursor)
        self.chat_display.tag_bind('hyperlink', '<Leave>', self._show_arrow_cursor)
        self.chat_display.tag_bind('hyperlink', '<Button-1>', self._open_link)
        
        # --- Input Frame ---
        input_frame = tk.Frame(self.main_frame, bg="#E6E6FA")
        input_frame.pack(padx=20, pady=10, fill=tk.X)

        self.user_input = tk.Entry(input_frame, font=("Helvetica", 12), bd=1, relief=tk.SOLID, bg="white", fg="#333333")
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 10))
        self.user_input.bind("<Return>", self.send_message_event)

        self.send_button = tk.Button(input_frame, text="Send", font=("Helvetica", 12, "bold"), bg="#4682B4", fg="white", bd=0, padx=20, pady=5, activebackground="#5F9EA0", activeforeground="white", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)
    
    def clear_chat(self):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state=tk.DISABLED)
        self.display_message("Bot", LANG_DATA[self.current_lang]['welcome'])

    # --- Hyperlink Helper Methods ---
    def _show_hand_cursor(self, event):
        self.chat_display.config(cursor="hand2")

    def _show_arrow_cursor(self, event):
        self.chat_display.config(cursor="")

    def _open_link(self, event):
        # get the index of the mouse click
        index = self.chat_display.index(f"@{event.x},{event.y}")
        # get the tags at that index
        tags = self.chat_display.tag_names(index)
        if "hyperlink" in tags:
            # get the link from the text
            link_range = self.chat_display.tag_prevrange("hyperlink", index)
            link = self.chat_display.get(link_range[0], link_range[1])
            webbrowser.open_new(link)

    def send_message_event(self, event):
        self.send_message()

    def send_message(self):
        user_text = self.user_input.get().strip()
        if user_text:
            self.display_message("You", user_text)
            self.process_command(user_text)
            self.user_input.delete(0, tk.END)

    def display_message(self, sender, message):
        self.chat_display.config(state=tk.NORMAL)
        
        sender_tag = 'user' if sender == "You" else 'bot'
        self.chat_display.insert(tk.END, f"{sender}: ", (sender_tag,))

        # Regex to find URLs
        url_pattern = re.compile(r'https?://\S+')
        urls = list(url_pattern.finditer(message))

        if not urls:
            self.chat_display.insert(tk.END, message + "\n\n")
        else:
            last_end = 0
            for match in urls:
                start, end = match.span()
                # Insert text before the link
                self.chat_display.insert(tk.END, message[last_end:start])
                # Insert the link with the hyperlink tag
                self.chat_display.insert(tk.END, message[start:end], ('hyperlink',))
                last_end = end
            # Insert any remaining text after the last link
            self.chat_display.insert(tk.END, message[last_end:] + "\n\n")

        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

    def process_command(self, command):
        command = command.lower()
        lang_data = LANG_DATA[self.current_lang]
        response = ""
        
        if 'otp' in command:
            self.display_message("Bot", lang_data['otp_warning'])
            return

        if self.state == "quiz":
            self.handle_quiz(command)
            return
        elif self.state == "image_prompt":
            self.handle_image_generation(command)
            return

        if command == 'info':
            response = f"{lang_data['info_intro']}\n\n{lang_data['info_content']}"
        elif command == 'security':
            response = f"{lang_data['security_tips']}\n\n{lang_data['security_content']}"
        elif command == 'quiz':
            self.start_quiz()
            return
        elif command == 'agri':
            response = f"{lang_data['agri_intro']}\n\n{lang_data['agri_content']}"
        elif command == 'health':
            response = f"{lang_data['health_intro']}\n\n{lang_data['health_content']}"
        elif command == 'skills':
            response = f"{lang_data['skills_intro']}\n\n{lang_data['skills_content']}"
        elif command == 'sanitation':
            response = f"{lang_data['sanitation_intro']}\n\n{lang_data['sanitation_content']}"
        elif command == 'emergency':
            response = f"{lang_data['emergency_intro']}\n\n{lang_data['emergency_content']}"
        elif command == 'digital_india':
            response = f"{lang_data['digital_india_intro']}\n\n{lang_data['digital_india_content']}"
        elif command == 'make_in_india':
            response = f"{lang_data['make_in_india_intro']}\n\n{lang_data['make_in_india_content']}"
        elif command == 'time':
            now = datetime.datetime.now()
            current_time = now.strftime("%I:%M %p")
            response = f"{lang_data['time']}{current_time}"
        elif command == 'date':
            now = datetime.datetime.now()
            current_date = now.strftime("%A, %B %d, %Y")
            response = f"{lang_data['date']}{current_date}"
        elif command == 'weather':
            now = datetime.datetime.now()
            hour = now.hour; month = now.month
            weather_desc = "Hot and humid with a chance of rain." if month in [3, 4, 5, 6, 7, 8] and 6 <= hour < 18 else "Warm and clear." if month in [3, 4, 5, 6, 7, 8] else "Cool and pleasant." if 6 <= hour < 18 else "Cold with a clear sky."
            response = lang_data['weather'].format(weather_desc=weather_desc)
        elif command == 'joke':
            response = f"{lang_data['joke_intro']}\n{random.choice(lang_data['jokes'])}"
        elif command == 'image':
            response = lang_data['image_prompt']
            self.state = "image_prompt"
        elif command == 'creator':
            response = lang_data['creator']
        elif command == 'help':
            response = lang_data['help_text']
        else:
            self.handle_nlp_response(command)
            return

        self.display_message("Bot", response)
        self.state = "initial"
        self.log_user_question(command, response)

    def handle_nlp_response(self, text):
        lang_data = LANG_DATA[self.current_lang]
        try:
            blob = TextBlob(text)
            sentiment_polarity = blob.sentiment.polarity
            
            if sentiment_polarity > 0.2:
                response = lang_data['nlp_positive']
            elif sentiment_polarity < -0.2:
                response = lang_data['nlp_negative']
            else:
                response = lang_data['nlp_neutral']

            self.display_message("Bot", response)
            self.log_user_question(text, response)
        except Exception:
            self.display_message("Bot", lang_data['unknown_command'])
            self.log_user_question(text, lang_data['unknown_command'])

    def start_quiz(self):
        self.state = "quiz"
        self.quiz_score = 0
        self.quiz_question_num = 1
        lang_data = LANG_DATA[self.current_lang]
        
        self.display_message("Bot", lang_data['quiz_intro'])
        self.display_message("Bot", f"{lang_data[f'q{self.quiz_question_num}']}\n{lang_data[f'q{self.quiz_question_num}_options']}")

    def handle_quiz(self, user_input):
        lang_data = LANG_DATA[self.current_lang]
        correct_answer = lang_data[f'q{self.quiz_question_num}_ans']

        if user_input.lower() == correct_answer:
            self.quiz_score += 1
            self.display_message("Bot", lang_data['correct'])
        else:
            self.display_message("Bot", f"{lang_data['incorrect']} {correct_answer.upper()}")
        
        self.quiz_question_num += 1

        if self.quiz_question_num <= 5:
            self.display_message("Bot", f"{lang_data[f'q{self.quiz_question_num}']}\n{lang_data[f'q{self.quiz_question_num}_options']}")
        else:
            self.end_quiz()

    def end_quiz(self):
        lang_data = LANG_DATA[self.current_lang]
        final_score = self.quiz_score
        total_questions = 5
        score_percentage = (final_score / total_questions) * 100
        
        if score_percentage >= 80:
            result_message = lang_data['quiz_end_excellent']
        elif score_percentage >= 50:
            result_message = lang_data['quiz_end_good']
        else:
            result_message = lang_data['quiz_end_average']

        response = f"{lang_data['your_score']}{final_score}/{total_questions}\n{result_message}"
        self.display_message("Bot", response)
        self.state = "initial"
        self.log_user_question("quiz completion", f"Score: {final_score}/{total_questions}")

    def handle_image_generation(self, prompt):
        lang_data = LANG_DATA[self.current_lang]
        if not prompt:
            self.display_message("Bot", "Please provide a valid description.")
            return

        self.display_message("Bot", lang_data['image_generating'].format(prompt=prompt))
        image_url = "https://dummyimage.com/600x400/000/fff&text=" + prompt.replace(" ", "+")
        
        response = f"{lang_data['image_link']}{image_url}"
        self.display_message("Bot", response)
        self.state = "initial"
        self.log_user_question(f"generate image: {prompt}", f"generated link: {image_url}")

    def log_user_question(self, user_text, bot_response):
        log_entry = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user_query": user_text,
            "bot_response": bot_response.strip(),
            "language": self.current_lang
        }
        try:
            with open("chat_log.json", "r+", encoding="utf-8") as file:
                data = json.load(file) if file.read(1) else []
                data.append(log_entry)
                file.seek(0)
                json.dump(data, file, indent=4, ensure_ascii=False)
        except (FileNotFoundError, json.JSONDecodeError):
            with open("chat_log.json", "w", encoding="utf-8") as file:
                json.dump([log_entry], file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()