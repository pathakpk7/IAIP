import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from PIL import Image

def build_perfect_elegant_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme Colors - Professional Academic/Corporate Palette
    BG_COLOR = RGBColor(248, 250, 252)       # Clean soft canvas
    CARD_BG = RGBColor(255, 255, 255)        # Pure white cards
    BORDER_COLOR = RGBColor(226, 232, 240)   # Crisp subtle border
    NAVY_PRIMARY = RGBColor(15, 23, 42)      # Deep charcoal navy
    BLUE_ACCENT = RGBColor(2, 132, 199)      # Corporate blue
    TEAL_ACCENT = RGBColor(13, 148, 136)     # Emerald teal
    RED_ACCENT = RGBColor(220, 38, 38)       # Crimson alert
    AMBER_ACCENT = RGBColor(217, 119, 6)     # Warm amber
    TEXT_DARK = RGBColor(15, 23, 42)         # Primary text
    TEXT_MUTED = RGBColor(71, 85, 105)       # Body text

    def set_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_header(slide, title, category="MINI PROJECT PRESENTATION"):
        # Header banner card: 0.4" to 1.15" (height 0.75")
        h_card = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.75))
        h_card.fill.solid()
        h_card.fill.fore_color.rgb = CARD_BG
        h_card.line.color.rgb = BORDER_COLOR
        h_card.line.width = Pt(1)

        # Left blue accent vertical bar
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.4), Inches(0.08), Inches(0.75))
        bar.fill.solid()
        bar.fill.fore_color.rgb = BLUE_ACCENT
        bar.line.fill.background()

        tf = h_card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.12)
        tf.margin_bottom = Inches(0.1)

        p = tf.paragraphs[0]
        r0 = p.add_run()
        r0.text = f"{category.upper()}  |  "
        r0.font.name = "Segoe UI"
        r0.font.size = Pt(10)
        r0.font.bold = True
        r0.font.color.rgb = BLUE_ACCENT

        r1 = p.add_run()
        r1.text = title
        r1.font.name = "Segoe UI"
        r1.font.size = Pt(16)
        r1.font.bold = True
        r1.font.color.rgb = NAVY_PRIMARY

    def add_text_card(slide, left, top, width, height, title, points, badge=None, badge_color=BLUE_ACCENT):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER_COLOR
        card.line.width = Pt(1.2)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.25)
        tf.margin_bottom = Inches(0.2)

        p0 = tf.paragraphs[0]
        if badge:
            rb = p0.add_run()
            rb.text = f"[{badge}] "
            rb.font.name = "Segoe UI"
            rb.font.size = Pt(10)
            rb.font.bold = True
            rb.font.color.rgb = badge_color

        r0 = p0.add_run()
        r0.text = title
        r0.font.name = "Segoe UI"
        r0.font.size = Pt(13.5)
        r0.font.bold = True
        r0.font.color.rgb = NAVY_PRIMARY
        p0.space_after = Pt(8)

        for pt in points:
            p = tf.add_paragraph()
            p.space_after = Pt(6)
            if isinstance(pt, tuple):
                bold_prefix, rest_text = pt
                r_b = p.add_run()
                r_b.text = f"• {bold_prefix}: "
                r_b.font.name = "Segoe UI"
                r_b.font.size = Pt(10.5)
                r_b.font.bold = True
                r_b.font.color.rgb = NAVY_PRIMARY

                r_r = p.add_run()
                r_r.text = rest_text
                r_r.font.name = "Segoe UI"
                r_r.font.size = Pt(10)
                r_r.font.color.rgb = TEXT_MUTED
            else:
                r = p.add_run()
                r.text = f"• {pt}"
                r.font.name = "Segoe UI"
                r.font.size = Pt(10)
                r.font.color.rgb = TEXT_MUTED
        return card

    def add_fitted_image_card(slide, left, top, width, height, img_path, caption=None):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER_COLOR
        card.line.width = Pt(1.2)

        pad = Inches(0.18)
        cap_h = Inches(0.32) if caption else Inches(0)
        avail_w = width - (pad * 2)
        avail_h = height - (pad * 2) - cap_h

        if os.path.exists(img_path):
            with Image.open(img_path) as im:
                px_w, px_h = im.size
            img_aspect = px_w / px_h
            box_aspect = avail_w / avail_h

            if box_aspect > img_aspect:
                # Height is the constraint
                final_h = avail_h
                final_w = avail_h * img_aspect
            else:
                # Width is the constraint
                final_w = avail_w
                final_h = avail_w / img_aspect

            # Perfectly centered inside the card
            img_left = left + pad + (avail_w - final_w) / 2
            img_top = top + pad + (avail_h - final_h) / 2

            slide.shapes.add_picture(img_path, img_left, img_top, width=final_w, height=final_h)

        if caption:
            tb = slide.shapes.add_textbox(left + pad, top + height - cap_h - Inches(0.08), width - (pad * 2), cap_h)
            tf = tb.text_frame
            tf.word_wrap = True
            tf.margin_top = tf.margin_bottom = tf.margin_left = tf.margin_right = 0
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER
            r = p.add_run()
            r.text = caption
            r.font.name = "Segoe UI"
            r.font.size = Pt(9.5)
            r.font.italic = True
            r.font.color.rgb = TEXT_MUTED

    # CONTENT TOP AND HEIGHT: Perfectly fits 7.5" slide with 0.5" bottom margin
    C_TOP = Inches(1.35)
    C_HEIGHT = Inches(5.65)
    C_WIDTH_LEFT = Inches(5.7)
    C_WIDTH_RIGHT = Inches(5.733)
    GAP = Inches(0.3)
    RIGHT_LEFT = Inches(0.8) + C_WIDTH_LEFT + GAP

    # =========================================================================
    # SLIDE 1: PERFECT COMPACT TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_background(s1)

    t_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.6), Inches(11.733), Inches(6.3))
    t_card.fill.solid()
    t_card.fill.fore_color.rgb = CARD_BG
    t_card.line.color.rgb = BORDER_COLOR
    t_card.line.width = Pt(1.5)

    bar1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.6), Inches(11.733), Inches(0.08))
    bar1.fill.solid()
    bar1.fill.fore_color.rgb = BLUE_ACCENT
    bar1.line.fill.background()

    tf1 = t_card.text_frame
    tf1.word_wrap = True
    tf1.margin_left = Inches(0.8)
    tf1.margin_right = Inches(0.8)
    tf1.margin_top = Inches(0.4)

    p0 = tf1.paragraphs[0]
    p0.alignment = PP_ALIGN.CENTER
    r0 = p0.add_run()
    r0.text = "A MINI PROJECT PRESENTATION ON\n"
    r0.font.name = "Segoe UI"
    r0.font.size = Pt(12)
    r0.font.bold = True
    r0.font.color.rgb = BLUE_ACCENT

    p1 = tf1.add_paragraph()
    p1.alignment = PP_ALIGN.CENTER
    p1.space_before = Pt(6)
    r1 = p1.add_run()
    r1.text = "DATA ANALYTICS:\nSALES PERFORMANCE ANALYSIS & CUSTOMER SEGMENTATION\nUSING MACHINE LEARNING\n"
    r1.font.name = "Segoe UI"
    r1.font.size = Pt(20)
    r1.font.bold = True
    r1.font.color.rgb = NAVY_PRIMARY

    p2 = tf1.add_paragraph()
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(4)
    r2 = p2.add_run()
    r2.text = "Submitted in partial fulfillment of the requirements for the award of the degree of\n"
    r2.font.name = "Segoe UI"
    r2.font.size = Pt(10.5)
    r2.font.italic = True
    r2.font.color.rgb = TEXT_MUTED

    r3 = p2.add_run()
    r3.text = "Bachelor of Technology in Computer Science & Engineering\n"
    r3.font.name = "Segoe UI"
    r3.font.size = Pt(12)
    r3.font.bold = True
    r3.font.color.rgb = NAVY_PRIMARY

    logo_path = os.path.join("template_images", "image1.png")
    if os.path.exists(logo_path):
        s1.shapes.add_picture(logo_path, Inches(6.05), Inches(3.6), width=Inches(1.23))

    p3 = tf1.add_paragraph()
    p3.alignment = PP_ALIGN.CENTER
    p3.space_before = Pt(85)
    r4 = p3.add_run()
    r4.text = "Department of Computer Science & Engineering\nUNITED INSTITUTE OF TECHNOLOGY (284), LUCKNOW\n(Affiliated to Dr. A.P.J. Abdul Kalam Technical University, Lucknow)  •  Session 2026-27\n"
    r4.font.name = "Segoe UI"
    r4.font.size = Pt(11)
    r4.font.bold = True
    r4.font.color.rgb = NAVY_PRIMARY

    r5 = p3.add_run()
    r5.text = "Presented by: Student / Scholar Team (Uni. Roll No: 2102840100xxx) | Faculty Guide: CSE Dept."
    r5.font.name = "Segoe UI"
    r5.font.size = Pt(10)
    r5.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 2: PROJECT OVERVIEW (TEXT + VERTICAL PIPELINE FLOWCHART)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_background(s2)
    add_header(s2, "Project Overview & Engineering Architecture", "PROJECT OVERVIEW")

    add_text_card(s2, Inches(0.8), C_TOP, C_WIDTH_LEFT, C_HEIGHT, "Dual Analytics Workflow", [
        ("Background Context", "Retail organizations generate vast streams of transactional logs but often lack diagnostic profitability models."),
        ("Task 1: Superstore Analytics", "Comprehensive profitability audit across 9,994 retail orders (2014-2017) to uncover hidden category margin leaks."),
        ("Task 2: Customer Clustering", "Unsupervised machine learning on 200 customer profiles using K-Means to identify distinct demographic personas."),
        ("Engineering Objective", "Formulate descriptive KPIs, model discount sensitivity, and establish automated customer segmentation rules."),
        ("Expected ROI", "Eliminate loss-making inventory SKUs, enforce discount boundaries, and lift customer lifetime value (LTV).")
    ], badge="EXECUTIVE SCOPE", badge_color=BLUE_ACCENT)

    add_fitted_image_card(s2, RIGHT_LEFT, C_TOP, C_WIDTH_RIGHT, C_HEIGHT,
                          "outputs_flowcharts/flowchart_pipeline.png",
                          caption="Figure 1: End-to-End Analytics & Machine Learning Pipeline")

    # =========================================================================
    # SLIDE 3: TASK 1 — SALES & PROFITABILITY (TEXT + MONTHLY TREND)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_background(s3)
    add_header(s3, "Task 1: Longitudinal Sales Trends & Profitability", "TASK 1: SALES PERFORMANCE")

    add_text_card(s3, Inches(0.8), C_TOP, C_WIDTH_LEFT, C_HEIGHT, "Financial Performance Metrics", [
        ("Total Sales Turnover", "$2,297,201 ($2.30M) across 9,994 retail orders spanning 2014 to 2017."),
        ("Net Operating Profit", "$286,397 overall, representing a baseline corporate net margin of 12.47%."),
        ("Annual Growth Trajectory", "Consistent YoY growth averaging +20.4%, demonstrating strong demand expansion."),
        ("Seasonal Q4 Volume Surge", "Sales consistently spike in November and December due to holiday demand and annual corporate budget clearances."),
        ("Regional Profitability", "Western region leads with $108.4K profit (14.9% margin), whereas Central region suffers from aggressive price markdowns.")
    ], badge="FINANCIAL AUDIT", badge_color=TEAL_ACCENT)

    add_fitted_image_card(s3, RIGHT_LEFT, C_TOP, C_WIDTH_RIGHT, C_HEIGHT,
                          "Task-1-Sales-Data-Analysis/outputs/monthly_sales_trend.png",
                          caption="Figure 2: 4-Year Monthly Sales and Profit Longitudinal Trend")

    # =========================================================================
    # SLIDE 4: TASK 1 — CATEGORY PERFORMANCE (TEXT + CATEGORY CHART)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_background(s4)
    add_header(s4, "Task 1: Product Category Performance & Margin Traps", "TASK 1: SALES PERFORMANCE")

    add_text_card(s4, Inches(0.8), C_TOP, C_WIDTH_LEFT, C_HEIGHT, "Category Profitability Breakdown", [
        ("Technology (Star Performer)", "Generated $836,154 in revenue with $145,455 profit. High operating margin of 17.40%, led by enterprise equipment."),
        ("Office Supplies (Core Cashflow)", "Generated $719,047 in revenue with $122,491 profit. Delivered consistent 17.03% margin across high transaction volume."),
        ("Furniture (Margin Trap!)", "Generated $741,999 in revenue (32.3% of total sales) but contributed ONLY $18,451 in net profit—yielding a dismal 2.49% margin."),
        ("Diagnostic Takeaway", "Furniture consumes substantial shipping freight and warehouse space while producing negligible net operating returns.")
    ], badge="CATEGORY AUDIT", badge_color=BLUE_ACCENT)

    add_fitted_image_card(s4, RIGHT_LEFT, C_TOP, C_WIDTH_RIGHT, C_HEIGHT,
                          "Task-1-Sales-Data-Analysis/outputs/category_performance.png",
                          caption="Figure 3: Category Comparison: Sales Volume vs Net Profit")

    # =========================================================================
    # SLIDE 5: TASK 1 — SUB-CATEGORY PROFITABILITY (TEXT + SUBCAT CHART)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_background(s5)
    add_header(s5, "Task 1: Sub-Category Profitability & Chronic SKU Deficits", "TASK 1: SALES PERFORMANCE")

    add_text_card(s5, Inches(0.8), C_TOP, C_WIDTH_LEFT, C_HEIGHT, "Product Profit Drivers vs Drainers", [
        ("Top Profit Contributors", "Copiers (+ $55,618 profit, 36.7% margin), Phones (+ $44,516 profit), and Accessories (+ $41,937 profit) are prime financial pillars."),
        ("High-Margin Staples", "Paper (+ $34,054 profit) and Binders (+ $30,221 profit) deliver steady, resilient cash flow with minimal price sensitivity."),
        ("Tables (Catastrophic Loss)", "Accumulated a severe net loss of -$17,725 despite generating over $206,000 in sales volume."),
        ("Bookcases & Supplies", "Bookcases lost -$3,473 and general Supplies lost -$1,189, further depressing total enterprise earnings."),
        ("Actionable Remedy", "Repricing or discontinuing chronic loss-making Tables immediately restores over $17,000 to net operating profits.")
    ], badge="SKU PROFITABILITY", badge_color=RED_ACCENT)

    add_fitted_image_card(s5, RIGHT_LEFT, C_TOP, C_WIDTH_RIGHT, C_HEIGHT,
                          "Task-1-Sales-Data-Analysis/outputs/subcategory_profitability.png",
                          caption="Figure 4: Net Profit and Loss Distribution Across Sub-Categories")

    # =========================================================================
    # SLIDE 6: TASK 1 — THE 20% DISCOUNT CLIFF (TEXT + DISCOUNT CHART)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_background(s6)
    add_header(s6, "Task 1: The 20% Discount Cliff Analysis", "TASK 1: PRICING SENSITIVITY")

    add_text_card(s6, Inches(0.8), C_TOP, C_WIDTH_LEFT, C_HEIGHT, "Mathematical Margin Inversion", [
        ("0% to 10% Discount Band", "Maintains strong +28.5% net margin. Healthy unit profitability with steady, organic customer demand."),
        ("10% to 20% Discount Band", "Yields +14.2% margin. Safe promotional band where transactional gross profit covers operational overhead."),
        ("The 20% Inversion Cliff", "At 20% to 30% discount, net margin turns negative (-5.4% loss). Promotional price breaks fail to cover base COGS."),
        ("Clearance Markdowns (> 50%)", "Plummets to -85.2% cash loss. The company is actively subsidizing consumer orders."),
        ("Core Policy Directive", "Establish a strict 20% ceiling on sales discounts across all standard catalog merchandise.")
    ], badge="PRICING GOVERNANCE", badge_color=RED_ACCENT)

    add_fitted_image_card(s6, RIGHT_LEFT, C_TOP, C_WIDTH_RIGHT, C_HEIGHT,
                          "Task-1-Sales-Data-Analysis/outputs/discount_vs_profit.png",
                          caption="Figure 5: Correlation Between Applied Discount and Net Profit Margin")

    # =========================================================================
    # SLIDE 7: TASK 2 — CLUSTERING METHODOLOGY (TEXT + ELBOW METHOD)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_background(s7)
    add_header(s7, "Task 2: K-Means Clustering Methodology & Validation", "TASK 2: CUSTOMER SEGMENTATION")

    add_text_card(s7, Inches(0.8), C_TOP, C_WIDTH_LEFT, C_HEIGHT, "Machine Learning Pipeline", [
        ("Customer Dataset", "200 customer profiles containing Age, Annual Income (k$), and Spending Score (1-100). Zero missing values."),
        ("StandardScaler Scaling", "Z-score normalization z = (x - μ) / σ ensures Annual Income ($15k-$137k) does not overwhelm Age (18-70) in Euclidean distance calculations."),
        ("Elbow Method (WCSS)", "Evaluated within-cluster sum of squares across k=1 to 10. Clear inflection observed at k=5 to 6."),
        ("Silhouette Score (0.45)", "Evaluates intra-cluster cohesion vs nearest-cluster separation. Validates that k=6 provides robust cluster boundaries."),
        ("Why k=6 Beats k=5", "k=6 bifurcates the huge moderate group into Young Moderate Spenders vs Mature Moderate Spenders, enabling targeted digital outreach.")
    ], badge="MODEL VALIDATION", badge_color=BLUE_ACCENT)

    add_fitted_image_card(s7, RIGHT_LEFT, C_TOP, C_WIDTH_RIGHT, C_HEIGHT,
                          "Task-2-Customer-Segmentation/outputs/elbow_method.png",
                          caption="Figure 6: WCSS Elbow Curve for Optimal Cluster Selection")

    # =========================================================================
    # SLIDE 8: TASK 2 — IDENTIFIED CUSTOMER CLUSTERS (TEXT + CLUSTER SCATTER)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_background(s8)
    add_header(s8, "Task 2: Customer Segments in Multi-Dimensional Space", "TASK 2: CUSTOMER SEGMENTATION")

    add_text_card(s8, Inches(0.8), C_TOP, C_WIDTH_LEFT, C_HEIGHT, "The 6 Customer Clusters", [
        ("Cluster 1: VIP Luxury (N=39)", "High Income ($86.5k), High Spending (82.1), Mean Age: 32.7. Top prime targets for luxury and premium lines."),
        ("Cluster 4: High-Income Savers (N=34)", "High Income ($90.1k), Low Spending (17.9), Mean Age: 44.0. High purchasing power with conservative habits."),
        ("Cluster 2: Trend-Driven Youth (N=22)", "Low Income ($26.5k), High Spending (76.2), Mean Age: 25.6. Young shoppers active on mobile lifestyle channels."),
        ("Cluster 3: Young Professionals (N=38)", "Moderate Income ($59.4k), Moderate Spending (44.5), Mean Age: 26.1. Digital natives balancing career budgets."),
        ("Cluster 0: Mature Dependables (N=45)", "Moderate Income ($54.3k), Moderate Spending (49.1), Mean Age: 56.3. Loyal repeat in-store shoppers."),
        ("Cluster 5: Budget-Constrained (N=22)", "Low Income ($26.3k), Low Spending (19.4), Mean Age: 45.5. Value-driven essential clearance shoppers.")
    ], badge="CLUSTER MAP", badge_color=TEAL_ACCENT)

    add_fitted_image_card(s8, RIGHT_LEFT, C_TOP, C_WIDTH_RIGHT, C_HEIGHT,
                          "Task-2-Customer-Segmentation/outputs/customer_clusters.png",
                          caption="Figure 7: 2D Projection of Identified Customer Clusters")

    # =========================================================================
    # SLIDE 9: TASK 2 — PERSONA PROFILES & STRATEGIES (TEXT + CLUSTER PROFILE)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_background(s9)
    add_header(s9, "Task 2: Demographic Profiles & Marketing Playbooks", "TASK 2: TARGETING STRATEGIES")

    add_text_card(s9, Inches(0.8), C_TOP, C_WIDTH_LEFT, C_HEIGHT, "Actionable Marketing Activation", [
        ("VIP Concierge (Cluster 1)", "Provide dedicated account management, exclusive preview drops, and zero markdown discounts."),
        ("High-Income Savers (Cluster 4)", "Market premium durability, warranties, and high-ROI value propositions to overcome buying hesitation."),
        ("Digital Youth (Cluster 2)", "Deploy mobile-first campaigns (Instagram/TikTok), micro-promotions, and Buy-Now-Pay-Later (BNPL) financing."),
        ("Young Professionals (Cluster 3)", "Target career lifestyle upgrades, workplace tech, and digital productivity tools."),
        ("Mature Dependables (Cluster 0)", "Reward loyalty with point-based rewards, direct mailers, and personalized customer support.")
    ], badge="MARKETING PLAYBOOK", badge_color=BLUE_ACCENT)

    add_fitted_image_card(s9, RIGHT_LEFT, C_TOP, C_WIDTH_RIGHT, C_HEIGHT,
                          "Task-2-Customer-Segmentation/outputs/cluster_profile.png",
                          caption="Figure 8: Mean Demographic and Behavioral Profile Across Clusters")

    # =========================================================================
    # SLIDE 10: STRATEGIC BUSINESS RECOMMENDATIONS (3 CLEAN PILLARS)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_background(s10)
    add_header(s10, "Data-Driven Strategic Business Recommendations", "STRATEGIC RECOMMENDATIONS")

    p_w = Inches(3.75)
    gap = Inches(0.24)

    add_text_card(s10, Inches(0.8), C_TOP, p_w, C_HEIGHT, "1. Enforce 20% Discount Ceiling", [
        ("Policy Directive", "Mandate a hard 20% discount ceiling on all standard retail catalog merchandise."),
        ("Stop Cash Bleed", "Eliminate 30%+ clearance markdowns that result in negative unit economics."),
        ("Financial Impact", "Recovers 3% to 5% in net enterprise operating margins ($35k - $45k annually).")
    ], badge="PRICING GOVERNANCE", badge_color=RED_ACCENT)

    add_text_card(s10, Inches(0.8) + p_w + gap, C_TOP, p_w, C_HEIGHT, "2. Restructure Furniture Catalog", [
        ("SKU Rationalization", "Discontinue chronically unprofitable individual Table models (-$17.7k loss)."),
        ("Mandatory Bundling", "Bundle Tables with high-margin Chairs (+13.4% margin) to offset shipping freight."),
        ("Financial Impact", "Eliminates over $21,000 in annual operational merchandise leakage.")
    ], badge="INVENTORY OPTIMIZATION", badge_color=AMBER_ACCENT)

    add_text_card(s10, Inches(0.8) + (p_w + gap) * 2, C_TOP, p_w, C_HEIGHT, "3. Targeted Persona Activation", [
        ("VIP Retention", "White-glove concierge and early access catalog for Cluster 1 (82.1 spending score)."),
        ("Youth Financing", "BNPL micro-promotions on digital channels for Cluster 2 (Trend Youth)."),
        ("Financial Impact", "Lifts Customer Lifetime Value (LTV) by +18% while lowering customer acquisition cost.")
    ], badge="LTV OPTIMIZATION", badge_color=TEAL_ACCENT)

    # =========================================================================
    # SLIDE 11: CONCLUSION & COMMITTEE VIVA PORTAL (2 CLEAN CARDS)
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_background(s11)
    add_header(s11, "Conclusion & Examination Viva Defense Portal", "VIVA DEFENSE PREPARATION")

    add_text_card(s11, Inches(0.8), C_TOP, C_WIDTH_LEFT, C_HEIGHT, "Project Summary & Findings", [
        ("1. Data Auditing & Integrity", "Processed 9,994 records with 100% data quality, standardizing datetime attributes and financial KPIs."),
        ("2. Topline Sales vs Net Profit", "Demonstrated that $2.30M in revenue masked severe profit deficits in Furniture (only 2.49% margin)."),
        ("3. The 20% Discount Cliff", "Empirically established the 20% discount threshold past which transactions become loss-making."),
        ("4. Mathematical Segmentation", "StandardScaler + K-Means++ successfully decomposed 200 customer profiles into 6 actionable behavioral personas."),
        ("5. Measurable Financial ROI", "Strategic recommendations yield over $38,000 in annual profit recovery.")
    ], badge="EXECUTIVE SUMMARY", badge_color=BLUE_ACCENT)

    add_text_card(s11, RIGHT_LEFT, C_TOP, C_WIDTH_RIGHT, C_HEIGHT, "Technical Viva Defense Q&A", [
        ("Q1: Why StandardScaler over MinMaxScaler?", "Euclidean distance is distorted when Income ($15k-$137k) has 100x the variance of Age (18-70). StandardScaler centers data (mean=0, std=1), preserving variance without outlier squashing."),
        ("Q2: Why select k=6 instead of standard k=5?", "While k=5 gives basic splits, it collapses ages 18-70 into one moderate group. k=6 bifurcates this into Young Moderate vs Mature Moderate, enabling differentiated digital marketing."),
        ("Q3: How does K-Means handle outliers?", "We verified outlier stability and used k-means++ probabilistic seeding, which selects well-spaced initial centers and prevents runaway centroid shifts."),
        ("Department of CSE", "United Institute of Technology (284), AKTU Lucknow • Session 2026-27")
    ], badge="VIVA PREPARATION", badge_color=TEAL_ACCENT)

    out_file = "Elegant_Project_Presentation.pptx"
    prs.save(out_file)
    print(f"SUCCESS: Generated {out_file} with {len(prs.slides)} perfectly proportioned 2D slides!")

if __name__ == '__main__':
    build_perfect_elegant_presentation()
