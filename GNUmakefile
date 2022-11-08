SITE ?= localhost

posts := $(shell bin/find_posts)
scss_files := $(shell find src/scss/ -type f -name "*.scss" -printf "%P\n")
css_files := $(scss_files:.scss=.css)
static_files := $(shell find src/static/ -type f -printf "%P\n")
upload_destination := $(shell bin/json_query src/sites/$(SITE).json .uploadDestination)

.PHONY: preview
preview: generate
	bin/json_query src/sites/$(SITE).json .urlBase
	cd out/$(SITE); python3 -m http.server

.PHONY: upload
upload: generate
	rsync --verbose --archive --delete out/$(SITE)/ $(upload_destination)/

.PHONY: generate
generate: $(posts:%=out/$(SITE)/%/index.html) \
          $(css_files:%=out/$(SITE)/%) \
          $(static_files:%=out/$(SITE)/%) \
          out/$(SITE)/index.html \
          out/$(SITE)/atom-feed.xml
	bin/hacks

out/$(SITE)/%/index.html: int/posts/%/post.yaml \
                  src/templates/post.html
	mkdir -p $(dir $@)
	mustache - src/templates/post.html \
	    < int/posts/$*/post.yaml \
	    > out/$(SITE)/$*/index.html

int/posts/%/post.yaml: int/posts/%/body.html \
                       src/blog.json \
                       src/posts/%/post.json
	mkdir -p $(dir $@)
	bin/merge_data \
	    site src/sites/$(SITE).json \
	    blog src/blog.json \
	    post src/posts/$*/post.json \
	    < int/posts/$*/body.html \
	    > int/posts/$*/post.yaml

int/posts/%/body.html: src/posts/%/body.html
	mkdir -p $(dir $@)
	cp $< $@

int/posts/%/body.html: int/posts/%/body.md
	mkdir -p $(dir $@)
	markdown < $< > $@

int/posts/%/body.md: src/posts/%/body.md
	mkdir -p $(dir $@)
	cp $< $@

int/posts/%/body.md: src/posts/%/body.foot.md
	mkdir -p $(dir $@)
	bin/footnotes.py < $< > $@

int/index.json: FORCE
	mkdir -p $(dir $@)
	bin/find_posts | bin/index_posts.py > int/index.json

int/index.yaml: int/index.json
	mkdir -p $(dir $@)
	bin/merge_data \
	    site src/sites/$(SITE).json \
	    blog src/blog.json \
	    index int/index.json \
	    < /dev/null \
	    > int/index.yaml

out/$(SITE)/index.html: int/index.yaml \
                src/templates/index.html
	mkdir -p $(dir $@)
	mustache - src/templates/index.html \
	    < int/index.yaml \
	    > out/$(SITE)/index.html

out/$(SITE)/atom-feed.xml: int/index.yaml \
                src/templates/atom-feed.xml
	mkdir -p $(dir $@)
	mustache - src/templates/atom-feed.xml \
	    < int/index.yaml \
	    > out/$(SITE)/atom-feed.xml

out/$(SITE)/%.css: src/scss/%.scss
	mkdir -p $(dir $@)
	sass --sourcemap=none $< $@

out/$(SITE)/%: src/static/%
	mkdir -p $(dir $@)
	cp $< $@

.PHONY: clean
clean:
	rm -r int
	rm -r out

.PHONY: FORCE
FORCE:
