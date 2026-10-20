/**
 * 4NOX WAV — System wielojęzyczności i tłumaczeń (PL ↔ EN)
 * Automatyczna podmiana treści tekstowych, atrybutów oraz cen (PLN -> EUR, ~400 zł = 100 €).
 * Zapamiętywanie wyboru w localStorage ('4nox-lang').
 */

const I18N = (() => {
    // ═════════════════════════════════════════════════════════
    // 1. CENNIK: REGUŁY PRZELICZANIA PLN -> EUR (400 zł ≈ 100 €)
    // ═════════════════════════════════════════════════════════
    const priceMap = {
        20: 5,
        50: 15,
        150: 40,
        200: 50,
        300: 75,
        400: 100,
        500: 125,
        700: 175,
        1000: 250,
        1500: 375,
        2000: 500
    };

    function plnToEur(val) {
        const num = parseInt(val, 10);
        if (isNaN(num)) return val;
        if (priceMap[num] !== undefined) return priceMap[num];
        const approx = num / 4;
        return Math.round(approx / 5) * 5 || Math.round(approx);
    }

    function convertPricesToEur(text) {
        if (!text) return text;
        let result = text;
        // OD 300 ZŁ / Od 300 zł / od 300 zł -> FROM 75 €
        result = result.replace(/(?:^|\b)(?:OD|Od)\s+(\d+)\s*(?:ZŁ|zł|z\u0142|Z\u0141)/gi, (match, p1) => `FROM ${plnToEur(p1)} €`);
        result = result.replace(/(?:^|\b)od\s+(\d+)\s*(?:ZŁ|zł|z\u0142|Z\u0141)/gi, (match, p1) => `from ${plnToEur(p1)} €`);
        // Samodzielne kwoty 300 ZŁ / 300 zł -> 75 €
        result = result.replace(/(\d+)\s*(?:ZŁ|zł|z\u0142|Z\u0141)/gi, (match, p1) => `${plnToEur(p1)} €`);
        // Jeśli gdziekolwiek zostało "OD" lub "Od" przed symbolem euro (np. "OD 75 €")
        result = result.replace(/(?:^|\b)(?:OD|Od)\s+(\d+\s*€)/g, 'FROM $1');
        result = result.replace(/(?:^|\b)od\s+(\d+\s*€)/g, 'from $1');
        // Jednostki i cennik
        result = result.replace(/\/ GODZ\./g, '/ HR');
        result = result.replace(/\/ godz\./g, '/ hr');
        result = result.replace(/(?:OD|od)\s+X\s*(?:zł|ZŁ)/gi, 'FROM X €');
        return result;
    }

    // ═════════════════════════════════════════════════════════
    // 2. SŁOWNIK TŁUMACZEŃ (PL -> EN)
    // ═════════════════════════════════════════════════════════
    const dict = {
        // ── Nawigacja ──
        "Portfolio": "Portfolio",
        "♫ Muzyczne": "♫ Music",
        "🎮 Game Dev": "🎮 Game Dev",
        "Oferta": "Pricing",
        "Twórcy": "Creators",
        "Social Media": "Social Media",
        "Kontakt": "Contact",

        // ── Hero Section ──
        "4NOX WAV Studio • Audio & Music Production": "4NOX WAV Studio • Audio & Music Production",
        "Tworzymy dźwięk, który pasuje do Twojej wizji.": "We create sound that fits your vision.",
        "Produkcja muzyczna": "Music Production",
        "Mix & Mastering": "Mix & Mastering",
        "Sound Design": "Sound Design",
        "Audio do gier": "Game Audio",
        "„Nie musisz wiedzieć dokładnie, czego potrzebujesz. Wystarczy, że wiesz, jaki efekt chcesz osiągnąć.”": "\"You don't need to know exactly what you need. Just know the effect you want to achieve.\"",
        "CHCĘ STWORZYĆ MUZYKĘ": "I WANT TO CREATE MUSIC",
        "POTRZEBUJĘ AUDIO DO PROJEKTU": "I NEED AUDIO FOR MY PROJECT",
        "3 poprawki w cenie": "3 revisions included",
        "Pełne przeniesienie praw": "Full rights transfer",
        "Faktury KSeF": "KSeF Invoices",
        "Jasny cennik OD X zł": "Clear pricing FROM X €",

        // ── Sekcja 2: Dwie Ścieżki ──
        "Dwie równorzędne ścieżki": "Two equal paths",
        "Czego potrzebujesz?": "What do you need?",
        "Niezależnie od tego, czy piszesz pierwszy wokalny kawałek, potrzebujesz miksu do wydania na Spotify, czy budujesz pełną oprawę dźwiękową gry lub filmu — prowadzimy projekt od A do Z.": "Whether you're writing your first vocal track, need a mix for Spotify release, or building full audio for a game or film — we handle the project from A to Z.",
        "Ścieżka A": "Path A",
        "Muzyka & Wokal": "Music & Vocals",
        "PRODUKCJA MUZYCZNA": "MUSIC PRODUCTION",
        "Od surowego pomysłu i melodii nucącej w głowie, przez pełną aranżację i podkład pod wokal, aż po profesjonalny mix i mastering gotowy na serwisy streamingowe.": "From a raw idea and melody in your head, through full arrangement and vocal backing, to professional mix and mastering ready for streaming platforms.",
        "Co realizujemy w tej ścieżce:": "What we deliver in this path:",
        "Produkcja całych utworów od podstaw (Ambient, Electronic, Folk, Hip-Hop, Pop, Cinematic)": "Full track production from scratch (Ambient, Electronic, Folk, Hip-Hop, Pop, Cinematic)",
        "Produkcja autorskich podkładów dla wokalistów i songwriterów": "Custom backing track production for vocalists and songwriters",
        "Aranżacja, sound design syntezatorów i budowanie instrumentału": "Arrangement, synth sound design and instrumental building",
        "Mix wielośladowy oraz mastering do standardów streamingowych": "Multi-track mix and mastering to streaming standards",
        "Dopasowanie pod styl, referencje i zamierzony klimat": "Style, reference and mood matching",
        "Ceny od": "Prices from",
        "(master) /": "(master) /",
        "(pełny utwór)": "(full track)",
        "(paczka 10 SFX / godz. montażu)": "(10 SFX pack / hour of editing)",
        "ZOBACZ CENY MUZYKI →": "SEE MUSIC PRICES →",
        "Ścieżka B": "Path B",
        "Gry • Wideo • Podcasty": "Games • Video • Podcasts",
        "AUDIO / SOUND DESIGN": "AUDIO / SOUND DESIGN",
        "Projektowanie autorskich efektów dźwiękowych, kinowych pejzaży dźwiękowych, montaż i czyszczenie mowy oraz pełne udźwiękowienie gier i filmów.": "Designing custom sound effects, cinematic soundscapes, voice editing and cleaning, and full audio for games and films.",
        "Efekty dźwiękowe (SFX) do gier, UI, czarów, broni, otoczenia": "Sound effects (SFX) for games, UI, spells, weapons, environments",
        "Kompleksowe udźwiękowienie zwiastunów, animacji i filmów": "Full audio for trailers, animations and films",
        "Montaż i czyszczenie dialogów, narracji, podcastów i słuchowisk": "Editing and cleaning dialogues, narration, podcasts and audio dramas",
        "Adaptacyjne audio i integracja silników gier (Unity, FMOD)": "Adaptive audio and game engine integration (Unity, FMOD)",
        "Paczki SFX na zamówienie z pełną licencją komercyjną": "Custom SFX packs with full commercial license",
        "ZOBACZ CENY AUDIO →": "SEE AUDIO PRICES →",

        // ── Sekcja 3: Pomysł ──
        "Dla wokalistów, twórców i osób prywatnych": "For vocalists, creators and individuals",
        "Masz tylko pomysł na utwór?": "Do you only have a song idea?",
        "Nucisz melodię na dyktafon w telefonie? Masz napisany tekst w notatniku? A może masz tylko ogólny klimat w głowie i kilka linków do piosenek, które Ci się podobają?": "Humming a melody into your phone? Have lyrics in a notepad? Or maybe you just have a general mood in mind and a few links to songs you like?",
        "Nie potrzebujesz wiedzy technicznej, nut ani profesjonalnego studia, żeby zacząć. Pomagamy przełożyć Twój zamysł na pełnoprawny, profesjonalny utwór: od harmonii i brzmienia, przez aranżację, aż po zgranie i mastering.": "You don't need technical knowledge, sheet music, or a professional studio to start. We help translate your idea into a full, professional track: from harmony and sound design, through arrangement, to final mixing and mastering.",
        "MAM POMYSŁ — POROZMAWIAJMY": "I HAVE AN IDEA — LET'S TALK",
        "Bez zobowiązań. Ocenimy wykonalność i podpowiemy najlepsze podejście.": "No commitment. We'll assess feasibility and suggest the best approach.",

        // ── Sekcja 4: Cennik ──
        "Przejrzyste zasady i brak ukrytych opłat": "Transparent rules and no hidden fees",
        "Wybierz zakres realizacji": "Choose your scope",
        "Od pojedynczego elementu po kompletną produkcję — zakres i cena zależą od projektu. W cenie każdej usługi:": "From a single element to complete production — scope and price depend on the project. Every service includes:",
        "3 poprawki": "3 revisions",
        "oraz pełne przeniesienie praw.": "and full rights transfer.",
        "Utwory": "Tracks",
        "Kompozycja & Produkcja Muzyczna": "Composition & Music Production",
        "Ambient / eksperymentalne": "Ambient / Experimental",
        "Podstawa": "Basic",
        "Prostsze formy ambientowe, eksperymentalne i atmosferyczne tworzone od podstaw pod tło, gry, medytację lub instalacje.": "Simpler ambient, experimental and atmospheric forms created from scratch for backgrounds, games, meditation or installations.",
        "Zakres realizacji:": "Scope of work:",
        "Kompozycja autorska": "Original composition",
        "Produkcja i synteza": "Production and synthesis",
        "Sound design tła": "Background sound design",
        "Mix & mastering": "Mix & mastering",
        "3 tury poprawek w cenie": "3 revision rounds included",
        "ZAPYTAJ O WYCENĘ": "GET A QUOTE",
        "Kompleksowo": "Full Package",
        "Pełna produkcja utworu": "Full track production",
        "Kompleksowa produkcja utworu — od pierwszego pomysłu lub ścieżki wokalnej do gotowego materiału emisyjnego.": "Complete track production — from the first idea or vocal track to broadcast-ready material.",
        "Kompozycja i aranżacja": "Composition and arrangement",
        "Autorski instrumental": "Custom instrumental",
        "Sound design i unikalne barwy": "Sound design and unique timbres",
        "Pełna produkcja pod wokal": "Full vocal-ready production",
        "Mix & mastering emisyjny": "Broadcast-ready mix & mastering",
        "Paczka stemsów (indywidualne ścieżki)": "Stems package (individual tracks)",
        "* Cena zależy od złożoności projektu i zakresu realizacji. Zawiera 3 tury poprawek i prawa majątkowe.": "* Price depends on project complexity and scope. Includes 3 revision rounds and commercial property rights.",
        "Montaż audio & Mix / Master": "Audio Editing & Mix / Master",
        "Postprodukcja & Dźwięk Mowy": "Post-production & Voice Audio",
        "Mix": "Mix",
        "Ścieżki": "Tracks",
        "Profesjonalne przygotowanie, edycja i miks dostarczonych ścieżek wielośladowych.": "Professional preparation, editing and mixing of delivered multi-track recordings.",
        "Edycja i czyszczenie": "Editing and cleaning",
        "Obróbka wokali": "Vocal processing",
        "Balans & przestrzeń": "Balance & space",
        "Processing kreatywny": "Creative processing",
        "WYCENA": "GET QUOTE",
        "Mastering": "Mastering",
        "Final": "Final",
        "Finalne przygotowanie materiału do publikacji i dystrybucji na Spotify, Apple Music i YT.": "Final preparation for publication and distribution on Spotify, Apple Music and YT.",
        "Mastering pasmowy": "Multiband mastering",
        "Optymalizacja LUFS": "LUFS optimization",
        "Współczesna dynamika": "Modern dynamics",
        "WAV 24-bit + MP3": "WAV 24-bit + MP3",
        "Montaż audio": "Audio Editing",
        "Podcast": "Podcast",
        "godzina gotowego materiału": "per hour of finished material",
        "Montaż podcastów, narracji, lektora i słuchowisk bez dodatkowego sound designu.": "Editing podcasts, narration, voice-overs and audio dramas without additional sound design.",
        "Montaż dialogów i mowy": "Dialogue and speech editing",
        "Czyszczenie oddechów i szumów": "Breath and noise cleaning",
        "Wyrównanie poziomów": "Level balancing",
        "Wklejenie podkładu klienta": "Client music bed insertion",
        "Full Audio": "Full Audio",
        "Montaż + SFX": "Editing + SFX",
        "Montaż materiału wraz z projektowaniem pełnej i immersyjnej warstwy dźwiękowej.": "Material editing with full immersive sound layer design.",
        "Montaż i czyszczenie głosu": "Voice editing and cleaning",
        "Projektowanie dedykowanych SFX": "Custom SFX design",
        "Ambience i efekty tła": "Ambience and background effects",
        "Miks całościowy": "Full mix",
        "* Stawka za godzinę dotyczy jednej godziny gotowego materiału audio.": "* Hourly rate applies to one hour of finished audio material.",
        "SFX / Sound Design": "SFX / Sound Design",
        "Efekty & Dźwięk do Gier / Wideo": "Effects & Sound for Games / Video",
        "Zestaw 10 SFX": "10 SFX Pack",
        "Paczka": "Pack",
        "10 autorskich efektów dźwiękowych przygotowanych ściśle pod specyfikację Twojego projektu.": "10 custom sound effects prepared strictly to your project specifications.",
        "Sound design (synteza / foley)": "Sound design (synthesis / foley)",
        "Edycja i processing": "Editing and processing",
        "Eksport gotowych plików (WAV 48/96kHz)": "Export of finished files (WAV 48/96kHz)",
        "Pełna licencja komercyjna": "Full commercial license",
        "WKRÓTCE": "COMING SOON",
        "Paczki sampli": "Sample Packs",
        "Sklep paczek sampli, bibliotek dźwiękowych i instrumentów wirtualnych — wkrótce.": "Sample packs, sound libraries and virtual instruments shop — coming soon.",
        "Kolekcja profesjonalnych bibliotek dźwiękowych w przygotowaniu i katalogowaniu.": "Collection of professional sound libraries in preparation and cataloging.",
        "NIEDOSTĘPNE": "UNAVAILABLE",
        "Pełne udźwiękowienie": "Full Audio Production",
        "WYCENA INDYWIDUALNA": "INDIVIDUAL QUOTE",
        "Kompleksowe udźwiękowienie filmu, gry, animacji, zwiastuna lub słuchowiska od A do Z.": "Comprehensive audio design for film, game, animation, trailer or audio drama from A to Z.",
        "Sound design wszystkich obiektów": "Sound design for all objects",
        "Efekty dźwiękowe & Foley": "Sound effects & Foley",
        "Wielowarstwowy ambience": "Multi-layered ambience",
        "Miks całościowy (i opcjonalny FMOD)": "Full mix (and optional FMOD)",
        "Opieka do wdrożenia / premiery": "Support until implementation / launch",
        "* Zakres i cena ustalane indywidualnie na podstawie briefu.": "* Scope and pricing set individually based on the brief.",
        "Nie wiesz, czego potrzebujesz?": "Not sure what you need?",
        "Opisz swój projekt, a bezpłatnie przygotujemy zakres realizacji i indywidualną wycenę.": "Describe your project and we'll prepare a free scope and individual quote.",

        // ── Jawne wpisy cenowe (dla pewności poza regexem) ──
        "OD 300 ZŁ": "FROM 75 €",
        "OD 700 ZŁ": "FROM 175 €",
        "OD 200 ZŁ": "FROM 50 €",
        "OD 150 ZŁ": "FROM 40 €",
        "OD 500 ZŁ": "FROM 125 €",
        "150 ZŁ": "40 €",
        "700 ZŁ": "175 €",
        "200 ZŁ": "50 €",
        "OD X zł": "FROM X €",

        // ── Sekcja 5: Portfolio ──
        "Realizacje i odsłuch": "Works and previews",
        "Wybrane realizacje 4NOX WAV": "Selected works by 4NOX WAV",
        "Posłuchaj, jak brzmi nasza praca: od piosenek i coverów wokalnych, przez udźwiękowienie gier indie, po atmosferyczne słuchowiska.": "Listen to our work: from songs and vocal covers, through indie game audio, to atmospheric audio dramas.",
        "Wszystkie": "All",
        "Game Audio": "Game Audio",
        "Sound Design & Słuchowiska": "Sound Design & Audio Dramas",
        "Rola 4NOX WAV:": "4NOX WAV role:",
        "Pełna produkcja muzyczna, mix & mastering, wideo": "Full music production, mix & mastering, video",
        "Autorska aranżacja i słowiański folk klimatyczny. Stworzenie wielowarstwowego instrumentarium, nagranie i miks partii wokalnych oraz mastering.": "Original arrangement and atmospheric Slavic folk. Creating multi-layered instrumentation, recording and mixing vocal parts and mastering.",
        "Posłuchaj na YouTube": "Listen on YouTube",
        "Kompozycja, synteza, miks, mastering, sound design": "Composition, synthesis, mix, mastering, sound design",
        "Klimatyczny utwór inspirowany słowiańskim folkiem i klimatem wiedźmińskim, łączący surowe instrumenty akustyczne z hybrydową syntezą.": "Atmospheric track inspired by Slavic folk and Witcher vibes, blending raw acoustic instruments with hybrid synthesis.",
        "Odsłuchaj na YouTube": "Listen on YouTube",
        "Soundtrack, motyw przewodni, produkcja muzyczna": "Soundtrack, main theme, music production",
        "Uroczy, baśniowy soundtrack do gry stworzonej przez zespół 8bitJelly. Melodia prowadząca, ciepłe instrumentarium i dynamiczne przejścia.": "Charming, fairy-tale soundtrack for a game created by 8bitJelly. Leading melody, warm instrumentation and dynamic transitions.",
        "ODSŁUCH AUDIO:": "AUDIO PREVIEW:",
        "Zobacz Projekt Gry →": "See Game Project →",
        "Pełna ścieżka dźwiękowa, adaptacyjna implementacja FMOD": "Full soundtrack, adaptive FMOD implementation",
        "Dynamiczna ścieżka do przygodowej gry fantasy. Muzyka reagująca na stan rozgrywki oraz stan zdrowia gracza w middleware FMOD.": "Dynamic soundtrack for a fantasy adventure game. Music reacting to gameplay state and player health in FMOD middleware.",
        "Zobacz Szczegóły Projektu →": "See Project Details →",
        "Pełny sound design potworów, grozy i otoczenia": "Full sound design for monsters, horror and environments",
        "Projekt dla ekipy VOXTEN. Immersyjne, mroczne audio do gry survival horror: niepokojący sound design, foley podziemi i budowanie napięcia ciszą.": "Project for VOXTEN team. Immersive, dark audio for a survival horror game: unsettling sound design, dungeon foley and building tension with silence.",
        "Zobacz Projekt Horroru →": "See Horror Project →",
        "Słuchowisko & SFX": "Audio Drama & SFX",
        "Reżyseria audio, sound design, montaż dialogów, miks": "Audio direction, sound design, dialogue editing, mix",
        "Profesjonalna realizacja fanowskiego słuchowiska w uniwersum Wiedźmina. Czyszczenie głosu lektorów, odgłosy walki mieczem, magia i karczemne tło.": "Professional production of a fan-made audio drama in The Witcher universe. Voice cleaning, sword fight sounds, magic and tavern ambience.",
        "Chcesz, aby Twój projekt brzmiał na tym samym poziomie?": "Want your project to sound at this level?",
        "Opowiedz nam o swojej wizji. Przygotujemy propozycję brzmieniową i konkretny plan działania.": "Tell us about your vision. We'll prepare a sonic proposal and a concrete action plan.",
        "ZRÓBMY TWÓJ PROJEKT": "LET'S MAKE YOUR PROJECT",

        // ── Sekcja 6: Proces ──
        "Krok po kroku": "Step by step",
        "Jak wygląda współpraca?": "How does collaboration work?",
        "Prosty, transparentny proces bez żargonu i bez nieporozumień. Wiesz dokładnie, co się dzieje na każdym etapie.": "Simple, transparent process without jargon or misunderstandings. You know exactly what happens at every stage.",
        "OPISUJESZ POMYSŁ": "DESCRIBE YOUR IDEA",
        "Piszesz do nas przez formularz lub maila. Może to być nagranie z dyktafonu, tekst, referencja z YouTube lub wstępna koncepcja gry.": "Write to us via the form or email. It can be a voice memo, lyrics, YouTube reference or an initial game concept.",
        "Czas odpowiedzi: do 24h": "Response time: up to 24h",
        "USTALAMY ZAKRES I CENĘ": "WE SET SCOPE AND PRICE",
        "Dobieramy odpowiedni wariant realizacji, ustalamy stały budżet, termin oraz liczbę poprawek (standardowo 3 tury w cenie). Zero niespodzianek.": "We choose the right option, set a fixed budget, deadline and number of revisions (3 rounds included by default). No surprises.",
        "Jasna umowa i warunki": "Clear contract and terms",
        "TWORZYMY I WERYFIKUJEMY": "WE CREATE AND VERIFY",
        "Przystępujemy do produkcji. Przesyłamy Ci wersje robocze (wip), słuchasz i zgłaszasz swoje uwagi. Wprowadzamy poprawki, aż brzmi idealnie.": "We start production. We send you work-in-progress versions, you listen and give feedback. We make revisions until it sounds perfect.",
        "Stały kontakt i feedback": "Constant contact and feedback",
        "ODBIERASZ GOTOWY MATERIAŁ": "YOU RECEIVE THE FINAL MATERIAL",
        "Po akceptacji otrzymujesz bezstratne pliki WAV (oraz MP3 i stemsy jeśli dotyczy), umowę o przeniesienie autorskich praw majątkowych i fakturę KSeF.": "Upon approval you receive lossless WAV files (plus MP3 and stems if applicable), a copyright transfer agreement and a KSeF invoice.",
        "100% praw komercyjnych": "100% commercial rights",

        // ── Sekcja 7: Twórcy ──
        "Ludzie za konsoletą": "People behind the console",
        "Poznaj ludzi stojących za 4NOX WAV": "Meet the people behind 4NOX WAV",
        "Za nazwą 4NOX WAV nie stoi bezduszna korporacja ani generatory AI. To my pracujemy nad każdym taktem, samplem i pasmem w Twoim projekcie.": "Behind 4NOX WAV there's no soulless corporation or AI generators. It's us working on every beat, sample and frequency band in your project.",
        "Właściciel • Kompozytor • Sound Designer": "Owner • Composer • Sound Designer",
        "Specjalizuję się w precyzyjnej syntezie dźwięku, aranżacji i kompozycji utworów. Skupiam się na technicznym wykonaniu wizji klienta — przekładam surowe wyobrażenie i emocję na wymierne, gęste brzmienie w miksie.": "I specialize in precise sound synthesis, arrangement and composition. I focus on the technical execution of the client's vision — translating raw imagination and emotion into tangible, dense sound in the mix.",
        "Współwłaściciel • Sound Designer • Realizator": "Co-owner • Sound Designer • Audio Engineer",
        "Moim żywiołem jest szczegółowy sound design, foley oraz intuicyjne budowanie klimatu, który idealnie siada pod obraz lub wokal. Dbam o to, by każda sekunda audio niosła ze sobą właściwy ładunek energii i przestrzeni.": "My element is detailed sound design, foley and intuitively building atmosphere that perfectly fits visuals or vocals. I make sure every second of audio carries the right charge of energy and space.",
        "Właściciel & Główny Reżyser Audio": "Owner & Lead Audio Director",
        "Współwłaściciel & Sound Designer": "Co-owner & Sound Designer",
        "Sound designer i kompozytor specjalizujący się w precyzyjnej syntezie dźwięku. Skupiam się na technicznym wykonaniu wizji, przekładając intuicję na wymierne efekty audio.": "Sound designer and composer specializing in precise sound synthesis. I focus on the technical execution of the vision, translating intuition into tangible audio results.",
        "Specjalista od szczegółowego sound designu oraz kompozytor polegający na swojej intuicji, aby wiernie oddać pożądany efekt.": "Detailed sound design specialist and composer relying on intuition to faithfully convey the desired effect.",
        "Postprodukcja Dialogów": "Dialogue Post-production",
        "Zobacz pełne bio i portfolio twórców →": "See full creator bios and portfolio →",

        // ── Sekcja 8: FAQ ──
        "Centrum wsparcia": "Support Center",
        "Często zadawane pytania (FAQ)": "Frequently Asked Questions (FAQ)",
        "Wszystko, co musisz wiedzieć przed rozpoczęciem współpracy: kwestie prawne, poprawki, formaty plików i warunki handlowe.": "Everything you need to know before starting: legal matters, revisions, file formats and commercial terms.",
        "Mam tylko pomysł / melodię na telefonie — czy możecie zrobić z tego cały utwór?": "I only have an idea / melody on my phone — can you make a full track from it?",
        "Tak, dokładnie tym się zajmujemy. Wystarczy, że prześlesz nam nawet proste nagranie z dyktafonu w telefonie, tekst lub 2–3 utwory referencyjne w zbliżonym klimacie. Dobierzemy tonację, stworzymy harmonię, zbudujemy pełny autorski podkład, a następnie poprowadzimy Cię przez nagranie wokalu i wykonamy finalny miks oraz mastering.": "Yes, that's exactly what we do. Just send us even a simple voice memo, lyrics or 2-3 reference tracks in a similar mood. We'll pick the key, create harmony, build a full custom backing track, then guide you through vocal recording and deliver the final mix and master.",
        "Czym różni się Mix od Masteringu i czego właściwie potrzebuję?": "What's the difference between Mix and Mastering, and what do I actually need?",
        "to praca na pojedynczych, surowych ścieżkach (np. osobno wokal, perkusja, bas, syntezatory) — dbamy o to, by żaden element nie zagłuszał innego, czyścimy pasma, nakładamy efekty i budujemy przestrzeń stereo.": "is work on individual raw tracks (e.g. separate vocal, drums, bass, synths) — ensuring no element masks another, cleaning frequency bands, applying creative processing, and building immersive stereo space.",
        "to ostatni krok na zmiksowanym już pliku stereo — nadaje utworowi ostateczny szlif, właściwą głośność komercyjną (LUFS), dynamikę i sprawia, że utwór brzmi świetnie zarówno w słuchawkach za 20 zł, jak i w samochodzie czy w klubie. Jeśli masz już gotowy miks i brakuje mu kopa — wystarczy mastering. Jeśli masz osobne ścieżki — potrzebujesz miksu i masteringu.": "is the final step on the already mixed stereo file — giving the track its commercial polish, proper loudness (LUFS), punch and ensuring it sounds great both in 5 € headphones and in a car or club. If your mix is finished and just lacks punch — mastering is enough. If you have separate stems — you need both mixing and mastering.",
        "Ile poprawek obejmują zlecenia komercyjne?": "How many revisions do commercial orders include?",
        "W cenie każdego zlecenia zawsze zawarte są": "Every order always includes",
        "3 tury poprawek": "3 revision rounds",
        ". Przy pełnej produkcji muzycznej koszt każdej kolejnej poprawki ponad pakiet wynosi 50 zł, natomiast przy miksie lub masteringu wynosi on 20 zł.": ". For full music production, the cost of each additional revision is 15 €, while for mix or mastering it is 5 €.",
        "Czy otrzymam umowę o przeniesienie autorskich praw majątkowych?": "Will I receive a copyright transfer agreement?",
        "Tak. Podpisujemy oficjalną umowę o dzieło z pełnym przeniesieniem autorskich praw majątkowych na wszystkich wymaganych polach eksploatacji (streaming, YouTube, telewizja, gra, sprzedaż cyfrowa). Gotowy utwór lub udźwiękowienie należy w 100% do Ciebie.": "Yes. We sign an official work contract with full transfer of copyright on all required fields of exploitation (streaming, YouTube, TV, games, digital sales). The finished track or audio belongs 100% to you.",
        "Czy wystawiacie faktury przez KSeF?": "Do you issue invoices via KSeF?",
        "Tak. Wystawiamy legalne faktury zgodnie z aktualnie obowiązującymi przepisami prawa, w tym za pośrednictwem Krajowego Systemu e-Faktur (KSeF).": "Yes. We issue legal invoices in accordance with current Polish law, including via the National e-Invoice System (KSeF).",
        "Czy możliwy jest zwrot przed finalizacją zlecenia i przesłaniem plików?": "Is a refund possible before the order is finalized and files are sent?",
        "Tak, pod warunkiem, że zlecenie nie zostało jeszcze sfinalizowane i nie otrzymałeś od nas gotowych plików w pełnej jakości bez znaków wodnych.": "Yes, provided the order has not yet been finalized and you have not received finished files in full quality without watermarks.",
        "W jakich formatach dostarczacie gotowe materiały audio?": "In what formats do you deliver finished audio materials?",
        "Standardowo dostarczamy nieskompresowane pliki WAV w jakości studyjnej (24-bit / 44.1 kHz lub 48 kHz / 96 kHz do wideo i silników gier) oraz dodatkowo pliki MP3 (320 kbps) do wygodnego odsłuchu mobilnego. Na życzenie przygotowujemy również wersje instrumentalne, acapella, wersje z podciętym wokalem oraz paczkę stemsów.": "As standard, we deliver uncompressed studio-grade WAV files (24-bit / 44.1 kHz or 48 kHz / 96 kHz for video and game engines) plus MP3 files (320 kbps) for convenient mobile listening. Upon request, we also prepare instrumental versions, acapella, lead-vocal-down versions, and stem packs.",
        "Pracujecie zdalnie czy stacjonarnie na Śląsku?": "Do you work remotely or on-site in Silesia?",
        "Działamy w obu modelach. Nasza baza to": "We operate in both models. Our home base is",
        "Żory (woj. śląskie)": "Żory (Silesia, Poland)",
        "— jeśli jesteś ze Śląska lub okolic (Katowice, Gliwice, Rybnik, Bielsko-Biała), możemy spotkać się osobiście. 90% naszych projektów realizujemy jednak w 100% zdalnie dla klientów z całej Polski i z zagranicy za pośrednictwem chmury, Discorda i platformy odsłuchowej.": "— if you're in Silesia or surrounding areas, we can meet in person. However, 90% of our projects are done 100% remotely for clients across Poland and worldwide via cloud storage, Discord, and streaming review platforms.",

        // ── Sekcja 9: Kontakt ──
        "Rozpocznij projekt": "Start a project",
        "Gotowy na współpracę?": "Ready to collaborate?",
        "Masz projekt? Pogadajmy.": "Have a project? Let's talk.",
        "Napisz do nas. Odpowiemy w ciągu 24 godzin z konkretną wyceną, terminem i wstępnym zakresem prac.": "Write to us. We'll respond within 24 hours with a specific quote, deadline and preliminary scope.",
        "Imię / Nick / Studio": "Name / Nickname / Studio",
        "Adres Email": "Email Address",
        "Wiadomość": "Message",
        "np. Jan Kowalski": "e.g. John Smith",
        "twoj@email.com": "your@email.com",
        "Opisz projekt, czego potrzebujesz, jaki efekt chcesz osiągnąć...": "Describe your project, what you need, what effect you want to achieve...",
        "WYŚLIJ WIADOMOŚĆ": "SEND MESSAGE",
        "Wolisz napisać bezpośrednio?": "Prefer to write directly?",
        "Kliknij, aby skopiować nasz adres e-mail:": "Click to copy our email address:",
        "Skopiuj Email": "Copy Email",
        "Kliknij, aby skopiować": "Click to copy",
        "Skopiowano!": "Copied!",

        // ── Podstrona Kontakt (contact.html) ──
        "Skontaktuj Się z Nami": "Contact Us",
        "Wysokiej Klasy Sound Design i Rozwiązania Audio": "High-end Sound Design & Audio Solutions",
        "Twoje Imię": "Your Name",
        "Twój Email": "Your Email",
        "W czym możemy pomóc?": "How can we help?",
        "Send Wiadomość": "Send Message",

        // ── Newsletter ──
        "Newsletter": "Newsletter",
        "Bądź na bieżąco": "Stay up to date",
        "Zapisz się, aby dostawać informacje o nowych utworach, ofertach specjalnych i aktualizacjach prosto na swoją skrzynkę.": "Subscribe to get updates about new tracks, special offers and news straight to your inbox.",
        "Twój adres email": "Your email address",
        "Zapisz się": "Subscribe",
        "Dziękujemy!": "Thank you!",
        "Zostałeś dodany do naszej listy mailingowej.": "You have been added to our mailing list.",

        // ── Stopka & Social ──
        "Obserwuj nasze najnowsze wydania": "Follow our latest releases",
        "Niezależne studio produkcji muzycznej, miksu, masteringu i sound designu. Żory, Śląsk / Zdalnie.": "Independent music production, mixing, mastering and sound design studio. Żory, Silesia / Remote.",
        "Portfolio Game Dev": "Portfolio Game Dev",
        "Portfolio Muzyczne": "Music Portfolio",
        "O nas": "About Us",
        "Wszelkie prawa zastrzeżone.": "All rights reserved.",

        // ── Podstrony Portfolio & Gry ──
        "Twórcy 4NOX": "4NOX Creators",
        "Poznaj wizjonerów audio, którzy tworzą następną generację sound designu.": "Meet the audio visionaries crafting the next generation of sound design.",
        "Produkcje muzyczne, miksy i mastering": "Music productions, mixes and mastering",
        "Audio do gier, sound design i produkcja muzyki": "Game audio, sound design and music production",
        "Powrót do strony głównej": "Back to homepage",
        "Powrót do strony głównej →": "Back to homepage →",
        "← Powrót": "← Back",
        "Powrót do Portfolio": "Back to Portfolio",
        "Zagraj na Steam": "Play on Steam",
        "O Ścieżce Dźwiękowej": "About the Soundtrack",
        "Próbki Ścieżki Dźwiękowej": "Soundtrack Samples",
        "Zrzuty Ekranu": "Screenshots",
        "Immersyjna ścieżka dźwiękowa i sound design do klimatycznej przygodowej gry logicznej": "Immersive soundtrack and sound design for an atmospheric puzzle adventure game",
        "Ta strona używa plików cookie, aby poprawić Twoje wrażenia.": "This site uses cookies to enhance your experience.",
        "Polityka Prywatności": "Privacy Policy",
        "Akceptuj": "Accept",
        "Zobacz Projekt": "View Project",
        "Rola:": "Role:",
        "Technologie:": "Technologies:",
        "Opis projektu": "Project description"
    };

    // ═════════════════════════════════════════════════════════
    // 3. SILNIK DRZEWA DOM
    // ═════════════════════════════════════════════════════════

    let currentLang = localStorage.getItem('4nox-lang') || 'pl';

    function translateText(originalText) {
        const trimmed = originalText.trim();
        if (!trimmed) return originalText;

        // Bezpośrednie dopasowanie w słowniku
        if (dict[trimmed]) {
            let translated = dict[trimmed];
            translated = convertPricesToEur(translated);
            return originalText.replace(trimmed, translated);
        }

        // Jeśli brak bezpośredniego dopasowania, sprawdzamy konwersję cen (np. "OD 300 ZŁ")
        let converted = convertPricesToEur(originalText);
        if (converted !== originalText) {
            return converted;
        }

        return originalText;
    }

    function processNode(node, toLang) {
        // Ignoruj elementy kodu, skryptów, styli, SVG
        if (node.nodeType === Node.ELEMENT_NODE) {
            const tag = node.tagName.toLowerCase();
            if (tag === 'script' || tag === 'style' || tag === 'svg' || tag === 'code' || tag === 'pre') return;

            // Zabezpieczenie atrybutów placeholder
            if (node.placeholder) {
                if (node._origPlaceholder === undefined) node._origPlaceholder = node.placeholder;
                if (toLang === 'pl') {
                    node.placeholder = node._origPlaceholder;
                } else {
                    const tr = dict[node._origPlaceholder.trim()];
                    node.placeholder = tr || node._origPlaceholder;
                }
            }

            // Atrybut title
            if (node.title) {
                if (node._origTitle === undefined) node._origTitle = node.title;
                if (toLang === 'pl') {
                    node.title = node._origTitle;
                } else {
                    const tr = dict[node._origTitle.trim()];
                    node.title = tr || node._origTitle;
                }
            }

            // Atrybut aria-label
            if (node.getAttribute && node.getAttribute('aria-label')) {
                if (node._origAriaLabel === undefined) node._origAriaLabel = node.getAttribute('aria-label');
                if (toLang === 'pl') {
                    node.setAttribute('aria-label', node._origAriaLabel);
                } else {
                    const tr = dict[node._origAriaLabel.trim()];
                    if (tr) node.setAttribute('aria-label', tr);
                }
            }

            // Rekurencja dla dzieci
            for (let i = 0; i < node.childNodes.length; i++) {
                processNode(node.childNodes[i], toLang);
            }
        }

        // Węzeł tekstowy
        if (node.nodeType === Node.TEXT_NODE) {
            if (node._origText === undefined) {
                node._origText = node.textContent;
            }

            if (toLang === 'pl') {
                node.textContent = node._origText;
            } else {
                node.textContent = translateText(node._origText);
            }
        }
    }

    function updateToggleButtons(lang) {
        const isPl = lang === 'pl';
        // Aktualizacja wszystkich przycisków na stronie (desktop i mobile)
        document.querySelectorAll('.lang-toggle-btn').forEach(btn => {
            btn.setAttribute('aria-label', isPl ? 'Switch to English' : 'Przełącz na język polski');
            btn.innerHTML = isPl
                ? '<span class="text-white font-bold">PL</span><span class="text-zinc-600">/</span><span class="text-zinc-500 font-normal">EN</span>'
                : '<span class="text-zinc-500 font-normal">PL</span><span class="text-zinc-600">/</span><span class="text-white font-bold">EN</span>';
        });

        // Wersje mobilne z etykietą tekstową
        document.querySelectorAll('.mobile-lang-label').forEach(el => {
            el.textContent = isPl ? 'PL' : 'EN';
        });
    }

    function updateHeadMeta(lang) {
        if (!document._origTitle) document._origTitle = document.title;
        const descMeta = document.querySelector('meta[name="description"]');
        if (descMeta && !descMeta._origDesc) descMeta._origDesc = descMeta.getAttribute('content');
        const ogTitle = document.querySelector('meta[property="og:title"]');
        if (ogTitle && !ogTitle._origContent) ogTitle._origContent = ogTitle.getAttribute('content');
        const ogDesc = document.querySelector('meta[property="og:description"]');
        if (ogDesc && !ogDesc._origContent) ogDesc._origContent = ogDesc.getAttribute('content');

        if (lang === 'en') {
            document.title = "4NOX WAV | Music Production, Mix & Mastering, Sound Design — Online Audio Studio";
            if (descMeta) descMeta.setAttribute('content', "4NOX WAV is a professional audio studio providing music production, mix & mastering, game audio and sound design. Working remotely for clients across Europe and worldwide. Transparent pricing from 40 €. 24h response time.");
            if (ogTitle) ogTitle.setAttribute('content', "4NOX WAV | Music Production, Mix & Mastering, Game Audio & Sound Design");
            if (ogDesc) ogDesc.setAttribute('content', "We create sound that fits your vision. Music production, mix & mastering, sound design and complete audio for games and films. Remote work across Europe, prices from 40 €.");
        } else {
            if (document._origTitle) document.title = document._origTitle;
            if (descMeta && descMeta._origDesc) descMeta.setAttribute('content', descMeta._origDesc);
            if (ogTitle && ogTitle._origContent) ogTitle.setAttribute('content', ogTitle._origContent);
            if (ogDesc && ogDesc._origContent) ogDesc.setAttribute('content', ogDesc._origContent);
        }
    }

    function applyLanguage(lang) {
        processNode(document.body, lang);
        document.documentElement.lang = lang;
        currentLang = lang;
        localStorage.setItem('4nox-lang', lang);
        updateToggleButtons(lang);
        updateHeadMeta(lang);
    }

    function toggle() {
        const next = currentLang === 'pl' ? 'en' : 'pl';
        applyLanguage(next);
    }

    function init() {
        // Podepnij nasłuchiwacze lub zainicjuj stan
        updateToggleButtons(currentLang);
        if (currentLang === 'en') {
            applyLanguage('en');
        }
    }

    return {
        init,
        toggle,
        applyLanguage,
        getCurrentLang: () => currentLang
    };
})();

// Inicjalizacja po załadowaniu drzewa DOM
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => I18N.init());
} else {
    I18N.init();
}
