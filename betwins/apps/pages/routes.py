from apps.pages import blueprint
from apps import content
import json, os, re, time
from flask import render_template, request, abort, redirect, url_for, current_app, jsonify
from jinja2 import TemplateNotFound


def _by_slug(items, slug):
    return next((i for i in items if i['slug'] == slug), None)


@blueprint.route('/')
def index():
    return render_template(
        'pages/index.html', segment='index',
        games=content.GAMES, tournaments=content.TOURNAMENTS, posts=content.POSTS[:3],
    )


@blueprint.route('/about-us')
def about_us():
    return render_template('pages/about-us.html', segment='about-us')


@blueprint.route('/games')
def games():
    q = request.args.get('q', '').strip().lower()
    cat = request.args.get('cat', '').strip()
    return render_template(
        'pages/games.html', segment='games',
        games=content.GAMES, filters=content.GAME_FILTERS,
        query=q, initial_cat=cat
    )


@blueprint.route('/live-casino')
def live_casino():
    return render_template(
        'pages/live-casino.html', segment='live-casino',
        tables=content.LIVE_TABLES, filters=content.LIVE_FILTERS
    )


@blueprint.route('/tournaments')
def tournaments():
    return render_template(
        'pages/tournaments.html', segment='tournaments',
        tournaments=content.TOURNAMENTS, filters=content.TOURNAMENT_FILTERS
    )


@blueprint.route('/vip-club')
def vip_club():
    return render_template(
        'pages/vip-club.html', segment='vip-club',
        tiers=content.VIP_TIERS, benefits=content.VIP_BENEFITS
    )


@blueprint.route('/jackpots')
def jackpots():
    return render_template(
        'pages/jackpots.html', segment='jackpots',
        jackpots=content.JACKPOTS, winners=content.WINNERS
    )


@blueprint.route('/lucky-draw')
def lucky_draw():
    return render_template('pages/lucky-draw.html', segment='lucky-draw')


@blueprint.route('/results')
def results():
    return render_template(
        'pages/results.html', segment='results',
        results=content.RESULTS
    )


@blueprint.route('/blog')
def blog():
    cat = request.args.get('cat', '').strip()
    tag = request.args.get('tag', '').strip()
    posts = content.POSTS
    if cat:
        posts = [p for p in posts if p['cat'].lower() == cat.lower()]
    return render_template(
        'pages/blog.html', segment='blog',
        posts=posts, active_cat=cat, active_tag=tag
    )


@blueprint.route('/blog-grid')
def blog_grid():
    return render_template('pages/blog-grid.html', segment='blog-grid', posts=content.POSTS)


# ---- detail pages (data driven) -------------------------------------------
@blueprint.route('/game-details')
def game_details_default():
    return redirect(url_for('pages_blueprint.game_details', slug=content.GAMES[0]['slug']))


@blueprint.route('/game-details/<slug>')
def game_details(slug):
    game = _by_slug(content.GAMES, slug)
    if not game:
        abort(404)
    related = [g for g in content.GAMES if g['slug'] != slug and set(g['cats']) & set(game['cats'])][:3]
    return render_template('pages/game-details.html', segment='game-details', game=game, related=related)


@blueprint.route('/tournament-details')
def tournament_details_default():
    return redirect(url_for('pages_blueprint.tournament_details', slug=content.TOURNAMENTS[0]['slug']))


@blueprint.route('/tournament-details/<slug>')
def tournament_details(slug):
    t = _by_slug(content.TOURNAMENTS, slug)
    if not t:
        abort(404)
    others = [x for x in content.TOURNAMENTS if x['slug'] != slug][:3]
    return render_template('pages/tournament-details.html', segment='tournament-details', t=t, others=others)


@blueprint.route('/blog-details')
def blog_details_default():
    return redirect(url_for('pages_blueprint.blog_details', slug=content.POSTS[0]['slug']))


@blueprint.route('/blog-details/<slug>')
def blog_details(slug):
    post = _by_slug(content.POSTS, slug)
    if not post:
        abort(404)
    idx = content.POSTS.index(post)
    prev_post = content.POSTS[idx - 1] if idx > 0 else None
    next_post = content.POSTS[idx + 1] if idx < len(content.POSTS) - 1 else None
    recent = [p for p in content.POSTS if p['slug'] != slug][:3]
    return render_template(
        'pages/blog-details.html', segment='blog-details', post=post,
        prev_post=prev_post, next_post=next_post, recent=recent
    )


@blueprint.route('/contact-us')
def contact_us():
    return render_template('pages/contact-us.html', segment='contact-us')


@blueprint.route('/faq')
def faq():
    return render_template('pages/faq.html', segment='faq')


@blueprint.route('/responsible-gaming')
def responsible_gaming():
    return render_template('pages/responsible-gaming.html', segment='responsible-gaming')


@blueprint.route('/privacy-policy')
def privacy_policy():
    return render_template('pages/privacy-policy.html', segment='privacy-policy')


@blueprint.route('/terms-conditions')
def terms_conditions():
    return render_template('pages/terms-conditions.html', segment='terms-conditions')


@blueprint.route('/sign-in')
def sign_in():
    return render_template('pages/sign-in.html', segment='sign-in')


@blueprint.route('/sign-up')
def sign_up():
    return render_template('pages/sign-up.html', segment='sign-up')


# ---- fallback for any other plain template ---------------------------------
@blueprint.route('/<template>')
def route_template(template):
    try:
        if not template.endswith('.html'):
            template += '.html'

        segment = get_segment(request)
        return render_template("pages/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('pages/404.html', segment='404'), 404

    except Exception:
        current_app.logger.exception('Error rendering %s', template)
        return render_template('pages/error-500.html', segment='500'), 500


@blueprint.app_errorhandler(404)
def not_found(_e):
    return render_template('pages/404.html', segment='404'), 404


@blueprint.app_errorhandler(500)
def server_error(_e):
    return render_template('pages/error-500.html', segment='500'), 500


# Helper - Extract current page name from request
def get_segment(request):
    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index'
        return segment
    except Exception:
        return None


# ---- form endpoints (contact, newsletter, sign-up, reviews, comments, reservation) -----
FORM_MESSAGES = {
    'contact': 'Thank you! Our concierge team at Mandovi Riverfront, Goa will get back to you within 24 hours.',
    'newsletter': 'You are on the royal guest list! Watch your inbox for tournament invitations and festive offers.',
    'signup': 'Your request has been submitted successfully. Our admin team will verify your details shortly - you will be notified by SMS / email once approved.',
    'review': 'Thank you for your review! It will appear once verified by our casino floor manager.',
    'comment': 'Thanks for joining the discussion! Your comment is awaiting moderation.',
    'reservation': 'Your salon / tournament seat reservation request is received. Our concierge will confirm via call or WhatsApp.',
}
EMAIL_RE = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
SENSITIVE = ('password', 'pass', 'card', 'cvv', 'otp')


@blueprint.route('/forms/<kind>', methods=['POST'])
def submit_form(kind):
    if kind not in FORM_MESSAGES:
        abort(404)

    payload = request.get_json(silent=True) or request.form.to_dict()
    clean = {}
    for key, value in payload.items():
        if any(word in key.lower() for word in SENSITIVE):
            continue                       # never persist secrets
        clean[str(key)[:60]] = str(value)[:2000]

    email = clean.get('email') or clean.get('c-email') or clean.get('auth-email')
    if email and not EMAIL_RE.match(email):
        return jsonify(ok=False, message='Please enter a valid email address.'), 400

    record = dict(kind=kind, at=time.strftime('%Y-%m-%d %H:%M:%S'), data=clean)
    try:
        os.makedirs(current_app.instance_path, exist_ok=True)
        with open(os.path.join(current_app.instance_path, 'submissions.jsonl'), 'a', encoding='utf-8') as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + '\n')
    except OSError:
        current_app.logger.exception('Could not store form submission')

    return jsonify(ok=True, message=FORM_MESSAGES[kind])
