export BLOG_DIR=.

SITE ?= localhost

posts := $(shell bin/find_posts)
scss_files := $(shell find src/scss/ -name "*.scss" -printf "%P\n")
css_files := $(scss_files:.scss=.css)

.PHONY: preview
preview: generate
	bin/json_query src/sites/$(SITE).json .urlBase
	cd out/$(SITE); python -m SimpleHTTPServer

.PHONY: generate
generate: $(posts:%=out/$(SITE)/%/index.html) \
          $(css_files:%=out/$(SITE)/%) \
          out/$(SITE)/index.html

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

out/$(SITE)/%.css: src/scss/%.scss
	mkdir -p $(dir $@)
	sass $< $@

.PHONY: clean
clean:
	rm -r int
	rm -r out

.PHONY: FORCE
FORCE:
