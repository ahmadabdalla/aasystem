#!/usr/bin/env ruby
# Package checks only; real host installation and invocation are separate.
require 'json'
require 'yaml'
require 'pathname'
require 'uri'

Dir.chdir(File.expand_path('..', __dir__))

def check(condition, message)
  abort "FAIL: #{message}" unless condition
end

portable = JSON.parse(File.read('plugin.json'))
claude = JSON.parse(File.read('.claude-plugin/plugin.json'))
check(portable['name'] == 'aasystem', 'Installation identity must remain aasystem')
check(portable['version'].is_a?(String) && portable['version'].match?(/\A(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)\z/), 'Use a stable X.Y.Z version')
%w[name version].each do |key|
  check(portable[key] == claude[key], "Manifest #{key} values differ")
end

required = %w[README.md SKILL_SYSTEM.md CODEX.md LICENSE PSTACK_LICENSE.txt MATT_POCOCK_LICENSE.txt skills/principles/INDEX.md skills/aapilot/SKILL.md skills/aapilot/agents/openai.yaml]
required.each { |path| check(File.file?(path), "Missing export file: #{path}") }
check(!File.exist?('skills/aasystem'), 'Former entry point must not remain')

skills = Dir.glob('skills/*/SKILL.md').sort
check(!skills.empty?, 'Skill tree is empty')
skills.each do |path|
  frontmatter = File.read(path).match(/\A---\s*\n(.*?)\n---\s*\n/m)
  check(frontmatter, "Missing metadata: #{path}")
  metadata = YAML.safe_load(frontmatter[1])
  check(metadata.is_a?(Hash), "Metadata must be a mapping: #{path}")
  check(metadata['name'] == File.basename(File.dirname(path)), "Skill name differs from directory: #{path}")
  check(metadata['description'].is_a?(String) && !metadata['description'].strip.empty?, "Missing description: #{path}")
  check(metadata['disable-model-invocation'] == true, "Explicit invocation policy missing: #{path}")
  adapter = YAML.safe_load(File.read(File.join(File.dirname(path), 'agents/openai.yaml')))
  check(adapter.is_a?(Hash) && adapter.dig('policy', 'allow_implicit_invocation') == false, "Adapter invocation policy differs: #{path}")
end

# The system inventory links every portable skill, catching incomplete exports.
inventory = File.read('SKILL_SYSTEM.md').scan(/\]\((skills\/[^)]+\/SKILL\.md)\)/).flatten.uniq
check(inventory.sort == skills, 'System inventory and portable skill tree differ')

# Only these two documented authoring placeholders are exempt from path checks.
placeholders = {
  'skills/bootstrap-verification/references/project-instructions.md' => %w[VERIFIER_PATH MAP_PATH]
}
documents = Dir.glob('skills/**/*.md') + %w[README.md SKILL_SYSTEM.md CODEX.md AGENTS.md CHANGELOG.md RELEASING.md]
links = 0
documents.each do |path|
  source = File.read(path).gsub(/```.*?```/m, '')
  source.scan(/\]\(([^\s)]+)(?:\s+"[^"\n]*")?\)/).flatten.each do |target|
    next if target.match?(/\A[a-z][a-z0-9+.-]*:/i) || target.start_with?('#')
    target = URI::DEFAULT_PARSER.unescape(target.split('#', 2)[0].delete_prefix('<').delete_suffix('>'))
    next if placeholders.fetch(path, []).include?(target)
    resolved = Pathname.new(File.dirname(path)).join(target).cleanpath
    check(resolved.exist?, "Missing link target in #{path}: #{target}")
    links += 1
  end
end

changelog = File.read('CHANGELOG.md')
notes = changelog.split(/^## \[#{Regexp.escape(portable['version'])}\]\s*$/)[1]
check(notes && !notes.split(/^## \[/, 2)[0].strip.empty?, 'Missing versioned release notes')
check(system('sh', '-n', 'skills/bootstrap-verification/assets/check-verification-output.sh'), 'Shipped helper syntax failed')
check(system('sh', 'skills/bootstrap-verification/assets/check-verification-output.sh'), 'Verification output guard failed')
puts "PASS: aasystem #{portable['version']}; #{skills.length} skills and adapters; #{links} local link paths; release notes."
puts 'Host installation, invocation, workflow evaluations and link anchors are separate checks.'
