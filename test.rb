package 'httpd' do
  action :install
end

service 'httpd' do
  action [:enable, :start]
end

file '/etc/motd'
  owner 'root'
  group 'root'
  mode '0644'
  content 'Hello world'
end

user 'Kalimuthu.Sowndapan' do
  comment 'DevOps Interview'
  shell '/bin/bash'
  password 'password'
  action :create
end

cron 'test' do
  hour '17'
  minute '45'
  command 'test'
end

timezone 'london' do
  timezone 'Europe/London'
  action :set
end