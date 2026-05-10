import { createClient } from 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.39.3/+esm';

const SUPABASE_URL = 'https://aswnttslekiedptmnalw.supabase.co';
const SUPABASE_ANON_KEY = 'sb_publishable_5MonrH6MrPn-0tN-9BKVDA_sPJopydG';

export const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
